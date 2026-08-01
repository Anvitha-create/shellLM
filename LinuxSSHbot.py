#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import os
import getpass
import argparse
import datetime
import shutil
from pathlib import Path
from dotenv import load_dotenv
from session_manager import SessionManager
from llm_provider import LLMProvider
from logger import HoneypotLogger

load_dotenv()

BANNER = """
shelLM - LLM-Powered Linux SSH Honeypot v2.0

"""

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["openai","ollama","anthropic"], default="anthropic")
    parser.add_argument("--model", default=None)
    parser.add_argument("--personality", default="default_v1")
    parser.add_argument("--trace", action="store_true")
    parser.add_argument("--cleaned", action="store_true")
    return parser.parse_args()

def load_personality(name):
    path = Path("personalities") / f"{name}.yml"
    if not path.exists():
        path = Path("personalities") / "default_v1.yml"
    import yaml
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)

def fake_login():
    SECRET_USER = "anvitha"
    SECRET_PASS = "123"
    print()
    attempts = 0
    while attempts < 3:
        username = input("login as: ")
        password = getpass.getpass("password: ")
        if username == SECRET_USER and password == SECRET_PASS:
            print()
            print("Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-91-generic x86_64)")
            print(" * Documentation:  https://help.ubuntu.com")
            print(" * Management:     https://landscape.canonical.com")
            print(" * Support:        https://ubuntu.com/pro")
            print()
            return True
        else:
            attempts += 1
            if attempts < 3:
                print("Permission denied, please try again.")
            else:
                print()
                print("anvitha@linux: Permission denied (publickey,password).")
                print("[*] Too many failed attempts. Connection closed.")
                return False

def run_honeypot(args):
    print(BANNER)
    if args.cleaned and Path("logs").exists():
        shutil.rmtree("logs")
        Path("logs").mkdir()
        print("[*] Logs cleared.")

    personality = load_personality(args.personality)
    session = SessionManager(personality=personality)
    provider = LLMProvider(provider=args.provider, model=args.model, personality=personality, trace=args.trace)
    logger = HoneypotLogger(session_id=session.session_id, trace=args.trace)

    print(f"[*] Provider   : {args.provider}")
    print(f"[*] Model      : {provider.model}")
    print(f"[*] Personality: {args.personality}")
    print(f"[*] Session ID : {session.session_id}")
    print(f"[*] Trace      : {args.trace}")
    print("-" * 55)
    print(f"Last login: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')} from 192.168.1.1")

    # Fake SSH login
    if not fake_login():
        session.save()
        return

    cwd = "/home/anvitha"

    try:
        while True:
            short = cwd.replace("/home/anvitha", "~")
            prompt = f"anvitha@linux:{short}$ "
            try:
                cmd = input(prompt)
            except (EOFError, KeyboardInterrupt):
                print("\n[*] Session ended.")
                break

            if not cmd.strip():
                continue
            if cmd.strip() in ("exit", "logout", "quit"):
                print("logout")
                break
            if cmd.strip() == "clear":
                os.system("cls")
                continue

            response, new_cwd = provider.execute(command=cmd, cwd=cwd, session_history=session.get_history())
            session.add_exchange(cmd, response)
            if new_cwd:
                cwd = new_cwd
            logger.log(cmd, response, cwd)
            print(response)

    except Exception as e:
        print(f"\n[!] Fatal error: {e}")
        if args.trace:
            import traceback
            traceback.print_exc()
    finally:
        session.save()
        print(f"\n[*] Session saved -> sessions/{session.session_id}.json")
        print(f"[*] Logs saved    -> logs/{session.session_id}.log")

if __name__ == "__main__":
    args = parse_args()
    run_honeypot(args)
