"""
llm_provider.py - Multi-provider LLM backend for shelLM
Uses static filesystem for consistent output, LLM only for unknown commands
"""

import os
from filesystem import handle_static_command

SYSTEM_PROMPT_BASE = """You are simulating a realistic Ubuntu 22.04 Linux server terminal for a cybersecurity honeypot.

Your job is to respond EXACTLY like a real Linux shell would — terminal output only, no explanations.

The user is: anvitha (uid=1000)
Hostname: linux
Home: /home/anvitha

=== RULES ===
1. Output ONLY what the terminal would print. No explanations, no extra text.
2. sudo ALWAYS fails: "anvitha is not in the sudoers file. This incident will be reported."
3. apt/apt-get ALWAYS fails with permission denied.
4. Unknown commands: "bash: <cmd>: command not found"
5. NEVER print [Current directory] or any meta-text.
6. NEVER use tree characters like, or any unicode box-drawing characters.
7. Use only plain ASCII text in all responses.
8. Keep responses short and exact - only what a real terminal prints.
"""

DEFAULT_MODELS = {
    "openai": "gpt-4o",
    "ollama": "llama3.2",
    "anthropic": "claude-sonnet-4-20250514",
}


class LLMProvider:
    def __init__(self, provider: str, model: str, personality: dict, trace: bool = False):
        self.provider = provider
        self.model = model or DEFAULT_MODELS.get(provider, "llama3.2")
        self.personality = personality
        self.trace = trace
        self._setup_client()

    def _setup_client(self):
        if self.provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        elif self.provider == "anthropic":
            import anthropic
            self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        elif self.provider == "ollama":
            import ollama
            self.client = ollama
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def execute(self, command: str, cwd: str, session_history: list) -> tuple:
        cmd = command.strip()

        if self.trace:
            print(f"\n[TRACE] -> CMD: {cmd}")

        # ── Extract just command strings for the `history` command ──────────
        # session_history entries are {"cmd": ..., "response": ..., "timestamp": ...}
        cmd_history = [entry["cmd"] for entry in session_history if isinstance(entry, dict) and "cmd" in entry]
        # Include current command so `history` shows it (like real bash)
        cmd_history.append(cmd)

        # ── Try static filesystem first — always consistent ───────────────
        static_out, new_cwd, handled = handle_static_command(
            cmd, cwd, session_history=cmd_history
        )

        if handled:
            if self.trace:
                print(f"[TRACE] <- STATIC: {repr(static_out[:80])}")
            return static_out, new_cwd

        # ── Fall back to LLM for unknown commands ─────────────────────────
        if self.trace:
            print(f"[TRACE] -> Sending to LLM {self.provider}/{self.model}")

        try:
            response_text = self._call_llm(cmd, cwd)
        except Exception as e:
            response_text = f"bash: {cmd}: command not found"
            if self.trace:
                print(f"[TRACE] LLM error: {e}")

        # Strip non-ASCII
        response_text = response_text.encode('ascii', errors='ignore').decode('ascii')

        if self.trace:
            print(f"[TRACE] <- LLM: {response_text[:80]}")

        return response_text, cwd

    def _call_llm(self, command: str, cwd: str) -> str:
        user_msg = f"[CWD: {cwd}]\n$ {command}"

        if self.provider == "openai":
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT_BASE},
                    {"role": "user", "content": user_msg}
                ],
                temperature=0.1,
                max_tokens=300
            )
            return resp.choices[0].message.content.strip()

        elif self.provider == "anthropic":
            resp = self.client.messages.create(
                model=self.model,
                max_tokens=300,
                system=SYSTEM_PROMPT_BASE,
                messages=[{"role": "user", "content": user_msg}]
            )
            return resp.content[0].text.strip()

        elif self.provider == "ollama":
            resp = self.client.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT_BASE},
                    {"role": "user", "content": user_msg}
                ]
            )
            return resp["message"]["content"].strip()
