"""
logger.py - Honeypot activity logger with optional trace logging
"""

import datetime
import json
from pathlib import Path

LOGS_DIR = Path("logs")

class HoneypotLogger:
    def __init__(self, session_id: str, trace: bool = False):
        LOGS_DIR.mkdir(exist_ok=True)
        self.session_id = session_id
        self.trace = trace
        self.log_path = LOGS_DIR / f"{session_id}.log"
        self.trace_path = LOGS_DIR / f"{session_id}_trace.log"
        self._write_header()

    def _write_header(self):
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "w", encoding='utf-8') as f:
            f.write(f"=== shelLM Honeypot Session Log ===\n")
            f.write(f"Session  : {self.session_id}\n")
            f.write(f"Started  : {ts}\n")
            f.write("=" * 40 + "\n\n")

    def log(self, command: str, response: str, cwd: str):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{ts}] CWD={cwd}\n$ {command}\n{response}\n{'-'*40}\n"
        with open(self.log_path, "a", encoding='utf-8') as f:
            f.write(entry)
        if self.trace:
            trace_entry = {
                "timestamp": ts,
                "cwd": cwd,
                "command": command,
                "response": response
            }
            with open(self.trace_path, "a", encoding='utf-8') as f:
                f.write(json.dumps(trace_entry) + "\n")

    def trace_log(self, data: dict):
        if not self.trace:
            return
        ts = datetime.datetime.now().isoformat()
        entry = {"timestamp": ts, **data}
        with open(self.trace_path, "a", encoding='utf-8') as f:
            f.write(json.dumps(entry) + "\n")