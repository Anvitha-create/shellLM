# ShelLM

**LLM-Powered Linux SSH Honeypot**

ShelLM is an AI-powered Linux SSH honeypot that simulates a realistic Linux terminal using Large Language Models (LLMs). It is designed to attract attackers, monitor their behavior, and collect intelligence in a safe environment.

Inspired by the original **ShelLM** from Stratosphere Laboratory, CTU Prague.

---

# Features

- AI-powered realistic Linux terminal
- Real SSH server using Paramiko
- Simulated SSH login with account lockout
- Session memory for consistent filesystem simulation
- Real-time Flask monitoring dashboard
- Windows desktop notifications
- Multiple personalities
- Multi-provider LLM support (Ollama, OpenAI, Anthropic)
- Detailed activity and trace logging

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Anvitha-create/shellLM.git
cd shellLM
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the environment file:

```bash
copy .env_TEMPLATE .env
```

Edit `.env` and add your API keys if using OpenAI or Anthropic.

If using Ollama:

```bash
ollama pull llama3.1:8b
```

---

# Usage

## Start the SSH Server

```bash
python ssh_server.py --provider ollama --model llama3.1:8b
```

## Start the Dashboard

```bash
python dashboard.py
```

Open:

```
http://localhost:5000
```

## Start the Local Honeypot

```bash
python LinuxSSHbot.py --provider ollama --model llama3.1:8b
```

---

# Command-Line Options

| Option | Description |
|---------|-------------|
| `--provider` | openai / anthropic / ollama |
| `--model` | Model name (example: llama3.1:8b) |
| `--personality` | Personality profile |
| `--trace` | Enable detailed trace logging |
| `--cleaned` | Clear previous logs before starting |

Example:

```bash
python LinuxSSHbot.py --provider ollama --model llama3.1:8b --personality default_v1 --trace
```

---

# Personalities

| Name | Description |
|------|-------------|
| default_v1 | Ubuntu developer workstation |
| Eman_v1 | FinTech backend engineer |
| Muris_v1 | DevOps engineer |

---

# Project Structure

```
shellLM/
│── LinuxSSHbot.py
│── ssh_server.py
│── dashboard.py
│── llm_provider.py
│── session_manager.py
│── logger.py
│── filesystem.py
│── requirements.txt
│── .env_TEMPLATE
│── personalities/
│── logs/
│── sessions/
```

---

# Example Commands

```
ls -al
pwd
whoami
cat notes.txt
cd Desktop
ps aux
history
uname -a
```

---

# Technologies Used

- Python 3
- Ollama
- Llama 3.1:8B
- Paramiko
- Flask
- PyYAML
- python-dotenv
- win10toast-persist

---

# Ethical Use

This project is intended for educational and research purposes only.

Only deploy it on systems you own or where you have explicit authorization.

See **EthicalConsiderations.md** for more information.

---

# Author

**Anvitha Shetty**

B.Tech Computer Science Engineering

Cybersecurity • AI • DevOps