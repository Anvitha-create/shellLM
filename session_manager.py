"""
session_manager.py - Manages honeypot session state and persistence
Carries over context from previous sessions for consistency.
"""

import json
import uuid
import datetime
from pathlib import Path


SESSIONS_DIR = Path("sessions")


class SessionManager:
    def __init__(self, personality: dict):
        SESSIONS_DIR.mkdir(exist_ok=True)
        self.session_id = self._generate_session_id()
        self.personality = personality
        self.history = []
        self.start_time = datetime.datetime.now().isoformat()
        self.previous_context = self._load_last_session()

    def _generate_session_id(self) -> str:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        uid = str(uuid.uuid4())[:8]
        return f"session_{ts}_{uid}"

    def _load_last_session(self) -> list:
        """Load last session's exchanges for continuity."""
        sessions = sorted(SESSIONS_DIR.glob("*.json"))
        if not sessions:
            return []
        try:
            with open(sessions[-1]) as f:
                data = json.load(f)
                return data.get("history", [])[-10:]  # last 10 exchanges
        except Exception:
            return []

    def get_history(self) -> list:
        """Return combined previous + current history."""
        return self.previous_context + self.history

    def add_exchange(self, cmd: str, response: str):
        self.history.append({
            "cmd": cmd,
            "response": response,
            "timestamp": datetime.datetime.now().isoformat()
        })

    def save(self):
        """Save current session to disk."""
        data = {
            "session_id": self.session_id,
            "start_time": self.start_time,
            "end_time": datetime.datetime.now().isoformat(),
            "personality": self.personality.get("name", "unknown"),
            "total_commands": len(self.history),
            "history": self.history
        }
        path = SESSIONS_DIR / f"{self.session_id}.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
