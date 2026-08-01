# shelLM — LLM-Powered Linux SSH Honeypot

Simulates a realistic Linux terminal using AI to trap and study attackers.  
Inspired by the original [shelLM](https://github.com/stratosphereips/shelLM) from Stratosphere Lab, CTU Prague.

```
███████╗██╗  ██╗███████╗██╗     ██╗     ███╗   ███╗
██╔════╝██║  ██║██╔════╝██║     ██║     ████╗ ████║
███████╗███████║█████╗  ██║     ██║     ██╔████╔██║
╚════██║██╔══██║██╔══╝  ██║     ██║     ██║╚██╔╝██║
███████║██║  ██║███████╗███████╗███████╗██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝
```

---

## Features

- **Realistic fake Linux filesystem** — consistent across commands and sessions
- **Session memory** — previous session context carried forward for consistency
- **Multiple personalities** — different user profiles (Eman, Muris, default)
- **Multi-provider** — OpenAI, Anthropic Claude, or Ollama (local/free)
- **Trace logging** — full request/response logs for analysis
- **sudo blocked** — always denied, incident reported
- **Correct non-command handling** — bash errors for unknown input

---

## Installation

```bash
# 1. Clone or unzip the project
cd shelLM_project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup your API key
cp env_TEMPLATE .env
# Edit .env and add your key (see below)
```

---

## Configuration (.env)

Open `.env` and fill in the key for whichever provider you use:

| Variable | Provider |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic Claude (default) |
| `OPENAI_API_KEY` | OpenAI GPT |
| `OLLAMA_BASE_URL` | Ollama local (no key needed) |

---

## Usage

```bash
python3 LinuxSSHbot.py
```

### With options:

```bash
# Use Anthropic Claude (default)
python3 LinuxSSHbot.py --provider anthropic --personality Eman_v1

# Use OpenAI
python3 LinuxSSHbot.py --provider openai --model gpt-4o --personality Muris_v1

# Use Ollama (local, free)
python3 LinuxSSHbot.py --provider ollama --model llama3.1:8b --personality default_v1

# Enable trace logs + clear old logs
python3 LinuxSSHbot.py --provider anthropic --trace --cleaned
```

### All flags:

| Flag | Description |
|---|---|
| `--provider` | `anthropic` / `openai` / `ollama` |
| `--model` | Model ID (auto-selected if not set) |
| `--personality` | Persona from `personalities/` folder |
| `--trace` | Enable detailed request/response logging |
| `--cleaned` | Clear old logs before starting |

---

## Personalities

| Name | Description |
|---|---|
| `default_v1` | Generic Ubuntu developer machine |
| `Eman_v1` | Fintech backend engineer (Stripe, Postgres) |
| `Muris_v1` | DevOps/sysadmin (AWS, Kubernetes, Terraform) |

Add your own by creating `personalities/yourname_v1.yml`.

---

## Project Structure

```
shelLM_project/
├── LinuxSSHbot.py        ← main entry point
├── llm_provider.py       ← multi-provider LLM calls
├── session_manager.py    ← session persistence & history
├── logger.py             ← activity + trace logging
├── requirements.txt
├── env_TEMPLATE          ← copy to .env
├── personalities/
│   ├── default_v1.yml
│   ├── Eman_v1.yml
│   └── Muris_v1.yml
├── sessions/             ← auto-created, stores JSON sessions
└── logs/                 ← auto-created, stores .log files
```

---

## Try These Commands

Once running, try:
```
ls -al
whoami
cat notes.txt
cd Desktop/projects && ls
cat webapp/config.py
sudo su
apt-get update
ps aux
history
uname -a
```

---

## Ethical Use

This tool is for **research and education only**.  
Only deploy on systems you own or have explicit permission to test.  
See `EthicalConsiderations.md` for full guidelines.
