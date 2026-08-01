"""
filesystem.py - Static fake filesystem for shelLM
Static commands = consistent attacker recon output
LLM commands = dynamic/realistic responses
"""

import datetime

FILESYSTEM = {
    "/home/anvitha": {
        "type": "dir",
        "contents": ["Desktop", "Documents", "Downloads", ".bashrc", ".profile", ".ssh", "notes.txt"]
    },
    "/home/anvitha/notes.txt": {
        "type": "file",
        "content": """TODO: change DB password, meeting at 3pm
API key: sk-proj-xK9mN2pQrT8vL4wE6uI1oY3aF5cH7jM0
project code: A12-2022
remind: backup server before friday"""
    },
    "/home/anvitha/.bashrc": {
        "type": "file",
        "content": """# ~/.bashrc: executed by bash(1) for non-login shells.
export PATH="$HOME/.local/bin:$PATH"
export EDITOR=vim
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias gs='git status'
alias gp='git pull'
PS1='\\u@\\h:\\w\\$ '"""
    },
    "/home/anvitha/.profile": {
        "type": "file",
        "content": """# ~/.profile: executed by the command interpreter for login shells.
if [ -n "$BASH_VERSION" ]; then
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi"""
    },
    "/home/anvitha/.ssh": {
        "type": "dir",
        "contents": ["authorized_keys", "known_hosts"]
    },
    "/home/anvitha/.ssh/authorized_keys": {
        "type": "file",
        "content": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC7vV5K9mN2pQ anvitha@linux"
    },
    "/home/anvitha/.ssh/known_hosts": {
        "type": "file",
        "content": "192.168.1.1 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAB\ngithub.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A"
    },
    "/home/anvitha/Desktop": {
        "type": "dir",
        "contents": ["projects", "resume.pdf"]
    },
    "/home/anvitha/Desktop/resume.pdf": {
        "type": "file",
        "content": "Binary file - PDF document"
    },
    "/home/anvitha/Desktop/projects": {
        "type": "dir",
        "contents": ["webapp", "scripts"]
    },
    "/home/anvitha/Desktop/projects/webapp": {
        "type": "dir",
        "contents": ["app.py", "config.py", "requirements.txt"]
    },
    "/home/anvitha/Desktop/projects/webapp/app.py": {
        "type": "file",
        "content": """from flask import Flask, request, jsonify
from config import DB_CONFIG, SECRET_KEY
import psycopg2

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT id, username, email FROM users")
    users = cur.fetchall()
    return jsonify(users)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    return jsonify({"token": SECRET_KEY, "status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)"""
    },
    "/home/anvitha/Desktop/projects/webapp/config.py": {
        "type": "file",
        "content": """# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'appdb',
    'user': 'admin',
    'password': 'Str0ng#DB_Pass2023!'
}

SECRET_KEY = 'jwt_sup3r_s3cr3t_2024_anvitha'
API_KEY = 'sk-proj-xK9mN2pQrT8vL4wE6uI1oY3aF5cH7jM0'
DEBUG = False
STRIPE_KEY = 'sk_live_51NxK9mTzXkPqR8vL4wE6uI'"""
    },
    "/home/anvitha/Desktop/projects/webapp/requirements.txt": {
        "type": "file",
        "content": """flask==2.3.2
psycopg2-binary==2.9.7
requests==2.31.0
python-dotenv==1.0.0
stripe==5.5.0
pyjwt==2.8.0"""
    },
    "/home/anvitha/Desktop/projects/scripts": {
        "type": "dir",
        "contents": ["backup.sh", "deploy.sh"]
    },
    "/home/anvitha/Desktop/projects/scripts/backup.sh": {
        "type": "file",
        "content": """#!/bin/bash
DB_PASS="Str0ng#DB_Pass2023!"
BACKUP_DIR="/var/backups/db"
DATE=$(date +%Y%m%d)
echo "Starting backup..."
pg_dump -U admin -h localhost appdb > $BACKUP_DIR/backup_$DATE.sql
echo "Backup complete: $BACKUP_DIR/backup_$DATE.sql"
aws s3 cp $BACKUP_DIR/backup_$DATE.sql s3://anvitha-backups/"""
    },
    "/home/anvitha/Desktop/projects/scripts/deploy.sh": {
        "type": "file",
        "content": """#!/bin/bash
SERVER="192.168.1.50"
USER="deploy"
KEY="~/.ssh/deploy_key"
echo "Deploying to $SERVER..."
ssh -i $KEY $USER@$SERVER 'cd /var/www/app && git pull && systemctl restart app'
echo "Deploy complete!"
echo "App running at http://$SERVER:5000" """
    },
    "/home/anvitha/Documents": {
        "type": "dir",
        "contents": ["secret.txt", "passwords_backup.txt", "work"]
    },
    "/home/anvitha/Documents/secret.txt": {
        "type": "file",
        "content": """-----BEGIN ENCRYPTED MESSAGE-----
U2FsdGVkX1+xK9mN2pQrT8vL4wE6uI1o
Y3aF5cH7jM0nK9mN2pQrT8vL4wE6uI1o
Yj3aF5cH7jM0nK9mN2pQrT8vL4wE6uI=
-----END ENCRYPTED MESSAGE-----"""
    },
    "/home/anvitha/Documents/passwords_backup.txt": {
        "type": "file",
        "content": """# Password Backup - DO NOT SHARE
# Created: 2024-01-15

Gmail: anvitha.dev@gmail.com / G00gl3#2024!
GitHub: anvitha_dev / GitH@b#Secure99
AWS Console: anvitha@company.com / @ws#Cl0ud2024
Database (prod): admin / Str0ng#DB_Pass2023!
Database (dev): devuser / D3v#Pass2023
Redis: r3d1s_s3cr3t_k3y!
JWT Secret: jwt_sup3r_s3cr3t_2024_anvitha
Stripe (live): sk_live_51NxK9mTzXkPqR8vL4wE6uI
SSH passphrase: S3cur3#SSH_2024"""
    },
    "/home/anvitha/Documents/work": {
        "type": "dir",
        "contents": ["report_q3.txt"]
    },
    "/home/anvitha/Documents/work/report_q3.txt": {
        "type": "file",
        "content": """Q3 2024 Report
==============
Revenue: $142,500
New Users: 1,243
Churn Rate: 2.3%
Server Costs: $3,200/month
DB queries/day: 2.4M
Uptime: 99.8%"""
    },
    "/home/anvitha/Downloads": {
        "type": "dir",
        "contents": ["tools.tar.gz"]
    },
    "/home/anvitha/Downloads/tools.tar.gz": {
        "type": "file",
        "content": "Binary file - tar.gz archive"
    },
    "/etc/passwd": {
        "type": "file",
        "content": """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
anvitha:x:1000:1000:Anvitha,,,:/home/anvitha:/bin/bash
postgres:x:1001:1001:PostgreSQL:/var/lib/postgresql:/bin/bash"""
    },
    "/etc/shadow": {
        "type": "file",
        "content": "cat: /etc/shadow: Permission denied"
    },
    "/etc/hostname": {"type": "file", "content": "linux"},
    "/etc/os-release": {
        "type": "file",
        "content": """PRETTY_NAME="Ubuntu 22.04.3 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
ID=ubuntu"""
    },
}

STATIC_COMMANDS = {
    # User info
    "whoami": "anvitha",
    "id": "uid=1000(anvitha) gid=1000(anvitha) groups=1000(anvitha),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev)",
    "who": "anvitha pts/0 2026-06-09 09:12 (10.213.95.1)",
    "w": """ 09:45:21 up 3 days,  2:14,  1 user
USER     TTY      FROM             LOGIN@   IDLE JCPU PCPU WHAT
anvitha  pts/0    10.213.95.1      09:12    0.00s 0.12s 0.00s bash""",
    "users": "anvitha",
    "groups": "anvitha adm cdrom dip plugdev",
    "last": "anvitha pts/0 10.213.95.1 Mon Jun  9 09:12   still logged in",
    "finger": "Login: anvitha          Name: Anvitha\nDirectory: /home/anvitha  Shell: /bin/bash",
    # System info
    "uname": "Linux",
    "uname -a": "Linux linux 5.15.0-91-generic #101-Ubuntu SMP Tue Nov 14 13:30:08 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux",
    "uname -r": "5.15.0-91-generic",
    "uname -m": "x86_64",
    "hostname": "linux",
    "hostnamectl": """   Static hostname: linux
         Icon name: computer-vm
           Chassis: vm
        Machine ID: a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4
           Boot ID: f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3
    Virtualization: kvm
  Operating System: Ubuntu 22.04.3 LTS
            Kernel: Linux 5.15.0-91-generic
      Architecture: x86-64""",
    "arch": "x86_64",
    "cat /etc/hostname": "linux",
    "uptime": " 09:45:21 up 3 days,  2:14,  1 user,  load average: 0.08, 0.12, 0.10",
    # Process
    "ps": """  PID TTY          TIME CMD
 1204 pts/0    00:00:00 bash
 1342 pts/0    00:00:00 ps""",
    "ps aux": """USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 168548  9876 ?        Ss   08:00   0:02 /sbin/init
root       423  0.0  0.0  15420  2048 ?        Ss   08:00   0:00 /usr/sbin/sshd
postgres   891  0.0  0.2 214356 18432 ?        Ss   08:00   0:01 postgres: checkpointer
anvitha   1203  0.0  0.3 612480 24576 ?        Sl   09:12   0:03 python3 app.py
anvitha   1204  0.0  0.1  21456  8192 pts/0    Ss   09:12   0:00 bash
anvitha   1342  0.0  0.0  21456  1024 pts/0    R+   09:45   0:00 ps aux""",
    "ps -ef": """UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 08:00 ?        00:00:02 /sbin/init
root       423     1  0 08:00 ?        00:00:00 /usr/sbin/sshd
anvitha   1203   423  0 09:12 pts/0    00:00:03 python3 app.py
anvitha   1204  1203  0 09:12 pts/0    00:00:00 bash""",
    # Network
    "ifconfig": """eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.213.95.35  netmask 255.255.255.0  broadcast 10.213.95.255
        ether 08:00:27:4b:2a:9f  txqueuelen 1000  (Ethernet)
        RX packets 45231  bytes 52428800 (52.4 MB)
        TX packets 12043  bytes 1843200 (1.8 MB)

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0""",
    "ip addr": """1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
    inet 10.213.95.35/24 brd 10.213.95.255 scope global eth0""",
    "ip a": """1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
    inet 10.213.95.35/24 brd 10.213.95.255 scope global eth0""",
    "netstat -an": """Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN
tcp        0      0 10.213.95.35:22         10.213.95.1:54231       ESTABLISHED""",
    "netstat -tulpn": """Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address   Foreign Address  State    PID/Program
tcp        0      0 0.0.0.0:22      0.0.0.0:*        LISTEN   423/sshd
tcp        0      0 0.0.0.0:5000    0.0.0.0:*        LISTEN   1203/python3
tcp        0      0 0.0.0.0:5432    0.0.0.0:*        LISTEN   891/postgres""",
    "arp": """Address      HWtype  HWaddress           Flags Iface
10.213.95.1  ether   00:20:50:25:1e:d2   C     eth0""",
    "route": """Kernel IP routing table
Destination  Gateway      Genmask        Flags Metric Iface
0.0.0.0      10.213.95.1  0.0.0.0        UG    100    eth0
10.213.95.0  0.0.0.0      255.255.255.0  U     100    eth0""",
    # Disk
    "df -h": """Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G  8.2G   11G  43% /
tmpfs           984M     0  984M   0% /dev/shm""",
    "df": """Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       20480000 8601600  11264000  44% /""",
    "lsblk": """NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk
sda1     8:1    0   20G  0 part /""",
    "mount": """/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)""",
    "du -sh": "8.2G    .",
    # Memory
    "free -h": """               total        used        free      shared  buff/cache   available
Mem:           1.9Gi       856Mi       321Mi        12Mi       756Mi       921Mi
Swap:          2.0Gi          0B       2.0Gi""",
    "free": """               total        used        free
Mem:         2000000      876544      328704
Swap:        2097148           0     2097148""",
    # Hardware
    "lscpu": """Architecture:            x86_64
CPU(s):                  2
Model name:              Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
CPU MHz:                 2400.000
L2 cache:                256K""",
    "dmesg": """[    0.000000] Linux version 5.15.0-91-generic
[    0.000000] BIOS-provided physical RAM map:
[    1.234567] eth0: renamed from vif1.0""",
    # Sudo/apt always block
    "sudo su": "anvitha is not in the sudoers file. This incident will be reported.",
    "sudo -l": "anvitha is not in the sudoers file. This incident will be reported.",
    "sudo apt-get update": "anvitha is not in the sudoers file. This incident will be reported.",
    "sudo apt update": "anvitha is not in the sudoers file. This incident will be reported.",
    "apt-get update": "E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)",
    "apt update": "E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)",
    "apt-get install": "E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)",
    # Echo env vars
    "echo $USER": "anvitha",
    "echo $HOME": "/home/anvitha",
    "echo $SHELL": "/bin/bash",
    "echo $PATH": "/home/anvitha/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "echo $PWD": "/home/anvitha",
    "echo $HOSTNAME": "linux",
    # Systemctl
    "systemctl status": """* sshd.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled)
   Active: active (running) since Mon 2026-06-09 08:00:01 UTC""",
    # Kernel modules
    "lsmod": """Module                  Size  Used by
nf_conntrack          172032  1
ip_tables              32768  1""",
    # Logging
    "journalctl": """-- Logs begin at Mon 2026-06-09 08:00:01 UTC --
Jun 09 08:00:01 linux sshd[423]: Server listening on 0.0.0.0 port 22
Jun 09 09:12:00 linux sshd[423]: Accepted password for anvitha""",
    # Text tools (no-arg versions)
    "grep": "Usage: grep [OPTION]... PATTERN [FILE]...",
    "awk": "Usage: awk [POSIX or GNU style options] -f progfile [--] file ...",
    "sed": "Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]...",
    "sort": "sort: no input files",
    "uniq": "uniq: missing operand",
    "cut": "cut: you must specify a list of bytes, characters, or fields",
    "tr": "tr: missing operand",
    "tee": "",
    "head": "head: missing file operand",
    "tail": "tail: missing file operand",
    "diff": "diff: missing operand",
    "diff3": "diff3: missing operand",
    "cmp": "cmp: missing operand",
    "join": "join: missing operand",
    "paste": "paste: missing operand",
    "split": "split: missing operand after 'split'",
    "rev": "",
    "tac": "tac: missing file operand",
    "od": "od: no input file specified",
    "fold": "fold: missing file operand",
    "expand": "expand: missing file operand",
    "unexpand": "unexpand: missing file operand",
    "fmt": "fmt: missing file operand",
    "col": "",
    "column": "column: missing operand",
    "colrm": "",
    "bc": "bc 1.07.1\nCopyright 1991-1994 Free Software Foundation\n(quit to exit)",
    "dc": "",
    "factor": "factor: missing operand",
    "expr": "expr: missing operand",
    "seq": "seq: missing operand",
    "printf": "",
    # File utilities (no-arg)
    "file": "file: missing file operand",
    "basename": "basename: missing operand",
    "dirname": "dirname: missing operand",
    "readlink": "readlink: missing operand",
    "ln": "ln: missing file operand",
    "shred": "shred: missing file operand",
    "look": "look: missing operand",
    "locate": "locate: no pattern to search for specified",
    "access": "access: missing operand",
    # Compression
    "tar": "tar: You must specify one of the blrRtux options",
    "gzip": "gzip: compressed data not written to a terminal.",
    "gunzip": "gunzip: compressed data not written to a terminal.",
    "zip": "Copyright (c) 1990-2008 Info-ZIP",
    "unzip": "UnZip 6.00 of 20 April 2009",
    "bzip2": "bzip2: I won't compress to a terminal.",
    "ar": "Usage: ar [emulation options] [-]{dmpqrstx}[abcDfilMNoPsSTuvV] [--plugin <name>] [member-name] [count] archive-file file...",
    # Checksum
    "md5sum": "md5sum: missing file operand",
    "cksum": "cksum: missing file operand",
    "sum": "sum: missing file operand",
    # System control - always deny
    "reboot": "Failed to set wall message, ignoring: Interactive authentication required.",
    "shutdown": "Failed to set wall message, ignoring: Interactive authentication required.",
    "halt": "Failed to set wall message, ignoring: Interactive authentication required.",
    "poweroff": "Failed to set wall message, ignoring: Interactive authentication required.",
    # User mgmt - deny modifications
    "passwd": "passwd: You may not view or modify password information for anvitha.",
    "chage": "chage: Permission denied.",
    "chfn": "chfn: PAM: Authentication failure",
    "chsh": "chsh: PAM: Authentication failure",
    "useradd": "useradd: Permission denied.",
    "userdel": "userdel: Permission denied.",
    "usermod": "usermod: Permission denied.",
    "groupadd": "groupadd: Permission denied.",
    "groupdel": "groupdel: Permission denied.",
    "groupmod": "groupmod: Permission denied.",
    "gpasswd": "gpasswd: Permission denied.",
    "grpck": "grpck: Permission denied.",
    "chpasswd": "chpasswd: Permission denied.",
    # Job scheduling
    "crontab": "no crontab for anvitha",
    "crontab -l": "no crontab for anvitha",
    "atq": "",
    "batch": "",
    # Network tools
    "ping": "ping: usage error: Destination address required",
    "curl": "curl: try 'curl --help' for more information",
    "wget": "wget: missing URL",
    "nc": "Ncat: You must specify a host to connect to. QUITTING.",
    "nslookup": "no servers could be reached",
    "host": "host: missing name or address",
    "traceroute": "traceroute: missing host operand",
    "tracepath": "tracepath: missing host operand",
    "nmcli": "eth0: connected to Wired connection 1",
    "iftop": "iftop: you must be root to run iftop",
    "iotop": "iotop: command not found",
    "vnstat": """Database updated: 2026-06-09 09:45:02
   eth0  /  daily

         day         rx      |     tx      |    total    |   avg. rate
     ------------------------+-------------+-------------+---------------
     2026-06-09    52.43 MB  |   1.80 MB   |   54.23 MB  |    5.10 kbit/s
     ------------------------+-------------+-------------+---------------
     estimated       62 MB   |     2 MB    |      64 MB  |""",
    "rsync": "rsync: [sender] missing source specification",
    "scp": "usage: scp [-346ABCOpqRrsTv] [-c cipher] [-D sftp_server_path] [-F ssh_config]\n           [-i identity_file] [-J destination] [-l limit] [-o ssh_option]\n           [-P port] [-S program] source ... target",
    "ssh": "usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]\n           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]",
    "rcp": "rcp: missing operand",
    "iwconfig": "lo        no wireless extensions.\neth0      no wireless extensions.",
    "iptables": "iptables v1.8.7 (nf_tables): no command specified",
    "ipcs": """------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status

------ Semaphore Arrays --------
key        semid      owner      perms      nsems""",
    "ipcrm": "ipcrm: missing operand",
    # Hardware/system info
    "lshw": "-bash: lshw: command not found",
    "lsusb": "Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub",
    "hdparm": "hdparm: missing device filename",
    "dmidecode": "dmidecode: Permission denied",
    "hwclock": "2026-06-09 09:45:22.823624+00:00",
    "acpi": "Battery 0: Discharging, 85%, 02:34:12 remaining",
    "iostat": """Linux 5.15.0-91-generic (linux)   06/09/2026   _x86_64_    (2 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.42    0.00    0.21    0.08    0.00   99.29

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               1.23        12.34         5.67     123456      56789""",
    "vmstat": """procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 328704  45678 712345    0    0     3     2   45   89  0  0 99  0  0""",
    "dstat": """----total-cpu-usage---- -dsk/total- -net/total- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw
  0   0  99   0   0   0|  12k  5.6k|   0     0 |   0     0 |  45    89""",
    "sar": "-bash: sar: command not found",
    "mpstat": """Linux 5.15.0-91-generic (linux)   06/09/2026   _x86_64_    (2 CPU)

09:45:21 AM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
09:45:21 AM  all    0.42    0.00    0.21    0.08    0.00    0.00    0.00    0.00    0.00   99.29""",
    "pidof": "pidof: usage error: no program name specified",
    "pmap": "pmap: missing operand",
    "strace": "strace: must have PROG [ARGS] or -p PID",
    "watch": "watch: missing operand",
    "kill": "kill: usage: kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]",
    "bg": "bash: bg: no job control",
    "fg": "bash: fg: no job control",
    "chrt": "chrt: missing argument",
    # Disk commands
    "fdisk": "fdisk: cannot open /dev/sda: Permission denied",
    "cfdisk": "cfdisk: cannot open /dev/sda: Permission denied",
    "sync": "",
    "dosfsck": "dosfsck: missing device",
    "dump": "-bash: dump: command not found",
    "restore": "-bash: restore: command not found",
    "dumpe2fs": "dumpe2fs: Permission denied while trying to open /dev/sda1",
    # Shell / scripting
    "alias": "alias ll='ls -alF'\nalias la='ls -A'\nalias l='ls -CF'\nalias gs='git status'\nalias gp='git pull'",
    "export": "declare -x EDITOR=\"vim\"\ndeclare -x HOME=\"/home/anvitha\"\ndeclare -x LOGNAME=\"anvitha\"\ndeclare -x PATH=\"/home/anvitha/.local/bin:/usr/local/bin:/usr/bin:/bin\"\ndeclare -x SHELL=\"/bin/bash\"\ndeclare -x USER=\"anvitha\"",
    "env": "SHELL=/bin/bash\nUSER=anvitha\nHOME=/home/anvitha\nPATH=/home/anvitha/.local/bin:/usr/local/bin:/usr/bin:/bin\nEDITOR=vim\nLANG=en_US.UTF-8",
    "printenv": "SHELL=/bin/bash\nUSER=anvitha\nHOME=/home/anvitha\nPATH=/home/anvitha/.local/bin:/usr/local/bin:/usr/bin:/bin\nEDITOR=vim\nLANG=en_US.UTF-8",
    "set": "BASH=/bin/bash\nHOME=/home/anvitha\nHOSTNAME=linux\nSHELL=/bin/bash\nUSER=anvitha",
    "declare": "",
    "type": "type: usage: type [-afptP] name [name ...]",
    "which": "which: no argument given",
    "exit": "",
    # Calendar
    "cal": datetime.datetime.now().strftime("""    %B %Y
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30"""),
    # mail / print / communication
    "wall": "",
    "write": "write: write: you have write permission turned off.",
    "mailq": "Mail queue is empty",
    "biff": "biff: not currently receiving mail",
    "eject": "eject: unable to eject, last error: Operation not permitted",
    "cupsd": "cupsd: Permission denied",
    # Script/session recording
    "script": "Script started, file is typescript",
    "scriptreplay": "scriptreplay: missing argument",
    # Misc
    "sleep": "",
    "yes": "y\ny\ny\n...",
    "true": "",
    "false": "",
    "clear": "\033[2J\033[H",
    "reset": "\033[2J\033[H",
    "man": "What manual page do you want?",
    "info": "info: missing operand",
    "help": "GNU bash, version 5.1.16(1)-release (x86_64-pc-linux-gnu)\nThese shell commands are defined internally. Type 'help' to see this list.",
    "less": "Missing filename",
    "more": "more: missing operand",
    "vim": "Vim: Warning: Output is not to a terminal",
    "vi": "Vim: Warning: Output is not to a terminal",
    "nano": "Error opening terminal: unknown.",
    "emacs": "emacs: standard input is not a tty",
    "python3": "Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>>",
    "python": "Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux",
    "pip3": "pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)",
    "pip": "pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)",
    "git": "usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]\n           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]\n           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]\n           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]\n           [--super-prefix=<path>] [--config-env=<name>=<envvar>]\n           <command> [<args>]",
    "git status": "fatal: not a git repository (or any of the parent directories): .git",
    "git log": "fatal: not a git repository (or any of the parent directories): .git",
    "git pull": "fatal: not a git repository (or any of the parent directories): .git",
    "curl --help": "Usage: curl [options...] <url>",
    "wget --help": "GNU Wget 1.21.2, a non-interactive network retriever.",
    "ss": """Netid  State   Recv-Q  Send-Q   Local Address:Port    Peer Address:Port
tcp    LISTEN  0       128          0.0.0.0:22           0.0.0.0:*
tcp    LISTEN  0       5            0.0.0.0:5432         0.0.0.0:*
tcp    ESTAB   0       0       10.213.95.35:22      10.213.95.1:54231""",
    "ss -tulpn": """Netid  State   Recv-Q  Send-Q   Local Address:Port    Peer Address:Port   Process
tcp    LISTEN  0       128          0.0.0.0:22           0.0.0.0:*       users:(("sshd",pid=423,fd=3))
tcp    LISTEN  0       5            0.0.0.0:5432         0.0.0.0:*       users:(("postgres",pid=891,fd=5))
tcp    LISTEN  0       5            0.0.0.0:5000         0.0.0.0:*       users:(("python3",pid=1203,fd=4))""",
    "lsof": """COMMAND     PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd        423     root    3u  IPv4  12345      0t0  TCP *:ssh (LISTEN)
python3    1203  anvitha    4u  IPv4  15678      0t0  TCP *:5000 (LISTEN)
postgres    891 postgres    5u  IPv4  13456      0t0  TCP *:postgresql (LISTEN)""",
    "lsof -i": """COMMAND     PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd        423     root    3u  IPv4  12345      0t0  TCP *:ssh (LISTEN)
python3    1203  anvitha    4u  IPv4  15678      0t0  TCP *:5000 (LISTEN)""",
    "nmap": "-bash: nmap: command not found",
    "nc -zv": "Ncat: Connection refused.",
    "telnet": "telnet: command not found",
    "ftp": "ftp: command not found",
}


# ─────────────────────────────────────────────────────────────
# Helper: resolve path
# ─────────────────────────────────────────────────────────────
def resolve_path(path: str, cwd: str) -> str:
    if path.startswith("/"):
        return path.rstrip("/") or "/"
    if path in ("~", ""):
        return "/home/anvitha"
    if path == "..":
        parts = cwd.rstrip("/").split("/")
        if len(parts) > 1:
            parts.pop()
        return "/".join(parts) or "/"
    if path == ".":
        return cwd
    return cwd.rstrip("/") + "/" + path


# ─────────────────────────────────────────────────────────────
# ls
# ─────────────────────────────────────────────────────────────
def handle_ls(args: str, cwd: str) -> str:
    target = cwd
    show_hidden = "-a" in args or "-la" in args or "-al" in args
    long_format = "-l" in args
    parts = args.split()
    for p in parts:
        if not p.startswith("-"):
            target = resolve_path(p, cwd)
            break
    node = FILESYSTEM.get(target)
    if not node:
        return f"ls: cannot access '{target}': No such file or directory"
    if node["type"] != "dir":
        return target
    all_items = node["contents"]
    if show_hidden:
        items = [".", ".."] + all_items
    else:
        items = [i for i in all_items if not i.startswith(".")]
    if long_format:
        lines = ["total " + str(len(items) * 4)]
        for item in items:
            full = target.rstrip("/") + "/" + item
            n = FILESYSTEM.get(full, {})
            is_dir = n.get("type") == "dir"
            perm = "drwxr-xr-x" if is_dir else "-rw-r--r--"
            size = "4096" if is_dir else str(len(n.get("content", "")))
            lines.append(f"{perm} 2 anvitha anvitha {size:>6} Jun  4 09:12 {item}")
        return "\n".join(lines)
    return "  ".join(items)


# ─────────────────────────────────────────────────────────────
# cat
# ─────────────────────────────────────────────────────────────
def handle_cat(args: str, cwd: str) -> str:
    path = args.strip()
    if not path:
        return ""
    target = resolve_path(path, cwd)
    node = FILESYSTEM.get(target)
    if not node:
        return f"cat: {path}: No such file or directory"
    if node["type"] == "dir":
        return f"cat: {path}: Is a directory"
    return node["content"]


# ─────────────────────────────────────────────────────────────
# cd
# ─────────────────────────────────────────────────────────────
def handle_cd(args: str, cwd: str) -> tuple:
    target = args.strip()
    if not target or target == "~":
        return "", "/home/anvitha"
    new_path = resolve_path(target, cwd)
    node = FILESYSTEM.get(new_path)
    if not node:
        return f"bash: cd: {target}: No such file or directory", cwd
    if node["type"] != "dir":
        return f"bash: cd: {target}: Not a directory", cwd
    return "", new_path


# ─────────────────────────────────────────────────────────────
# tree  — DYNAMIC, built from FILESYSTEM
# ─────────────────────────────────────────────────────────────
def handle_tree(cwd: str) -> str:
    root_node = FILESYSTEM.get(cwd)
    if not root_node or root_node["type"] != "dir":
        return f"tree: '{cwd}': No such file or directory"

    lines = ["."]
    dir_count = [0]
    file_count = [0]

    def _recurse(path: str, prefix: str):
        node = FILESYSTEM.get(path)
        if not node or node["type"] != "dir":
            return
        items = node.get("contents", [])
        for i, item in enumerate(items):
            is_last = (i == len(items) - 1)
            connector = "+-- " if is_last else "+-- "
            child_path = path.rstrip("/") + "/" + item
            child_node = FILESYSTEM.get(child_path, {})
            is_dir = child_node.get("type") == "dir"
            lines.append(prefix + connector + item)
            if is_dir:
                dir_count[0] += 1
                extension = "    " if is_last else "|   "
                _recurse(child_path, prefix + extension)
            else:
                file_count[0] += 1

    _recurse(cwd, "")
    lines.append("")
    lines.append(f"{dir_count[0]} directories, {file_count[0]} files")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# find
# ─────────────────────────────────────────────────────────────
def handle_find(args: str, cwd: str) -> str:
    results = []
    for path in FILESYSTEM:
        if path.startswith(cwd):
            results.append(path)
    return "\n".join(sorted(results)) if results else ""


# ─────────────────────────────────────────────────────────────
# wc
# ─────────────────────────────────────────────────────────────
def handle_wc(args: str, cwd: str) -> str:
    path = args.strip().split()[-1] if args.strip() else ""
    if not path:
        return "wc: missing file operand"
    target = resolve_path(path, cwd)
    node = FILESYSTEM.get(target)
    if not node:
        return f"wc: {path}: No such file or directory"
    content = node.get("content", "")
    lines = content.count("\n") + 1
    words = len(content.split())
    chars = len(content)
    return f" {lines} {words} {chars} {path}"


# ─────────────────────────────────────────────────────────────
# history  — needs session_history passed in
# ─────────────────────────────────────────────────────────────
def handle_history(args: str, session_history: list) -> str:
    """
    session_history is a list of command strings in chronological order.
    Pass the full list from your session tracker.
    """
    if not session_history:
        return ""
    # optional: `history N` shows last N entries
    limit = None
    try:
        n = int(args.strip())
        limit = n
    except (ValueError, TypeError):
        pass

    entries = session_history if limit is None else session_history[-limit:]
    # history numbering starts at 1 and counts from the beginning of the session
    offset = len(session_history) - len(entries) + 1
    lines = []
    for i, cmd in enumerate(entries, start=offset):
        lines.append(f"  {i:4d}  {cmd}")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# grep / awk / sed / head / tail with args
# ─────────────────────────────────────────────────────────────
def handle_grep(args: str, cwd: str) -> str:
    """Basic grep simulation: grep PATTERN FILE"""
    parts = args.strip().split(None, 1)
    if len(parts) < 2:
        return "Usage: grep [OPTION]... PATTERN [FILE]..."
    pattern, rest = parts[0], parts[1]
    filepath = rest.strip()
    target = resolve_path(filepath, cwd)
    node = FILESYSTEM.get(target)
    if not node:
        return f"grep: {filepath}: No such file or directory"
    if node["type"] == "dir":
        return f"grep: {filepath}: Is a directory"
    matches = [line for line in node["content"].splitlines() if pattern.lower() in line.lower()]
    return "\n".join(matches)


def handle_head(args: str, cwd: str) -> str:
    parts = args.strip().split()
    n = 10
    filepath = ""
    i = 0
    while i < len(parts):
        if parts[i] == "-n" and i + 1 < len(parts):
            try:
                n = int(parts[i + 1])
                i += 2
                continue
            except ValueError:
                pass
        elif parts[i].startswith("-") and len(parts[i]) > 1:
            try:
                n = int(parts[i][1:])
                i += 1
                continue
            except ValueError:
                pass
        else:
            filepath = parts[i]
        i += 1
    if not filepath:
        return "head: missing file operand"
    target = resolve_path(filepath, cwd)
    node = FILESYSTEM.get(target)
    if not node:
        return f"head: cannot open '{filepath}' for reading: No such file or directory"
    lines = node["content"].splitlines()
    return "\n".join(lines[:n])


def handle_tail(args: str, cwd: str) -> str:
    parts = args.strip().split()
    n = 10
    filepath = ""
    i = 0
    while i < len(parts):
        if parts[i] == "-n" and i + 1 < len(parts):
            try:
                n = int(parts[i + 1])
                i += 2
                continue
            except ValueError:
                pass
        elif parts[i].startswith("-") and len(parts[i]) > 1:
            try:
                n = int(parts[i][1:])
                i += 1
                continue
            except ValueError:
                pass
        else:
            filepath = parts[i]
        i += 1
    if not filepath:
        return "tail: missing file operand"
    target = resolve_path(filepath, cwd)
    node = FILESYSTEM.get(target)
    if not node:
        return f"tail: cannot open '{filepath}' for reading: No such file or directory"
    lines = node["content"].splitlines()
    return "\n".join(lines[-n:])


def handle_sed(args: str, cwd: str) -> str:
    """Basic sed s/old/new/ simulation"""
    parts = args.strip().split(None, 1)
    if len(parts) < 2:
        return "Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]..."
    expr = parts[0]
    filepath = parts[1].strip()
    if not expr.startswith("s/"):
        return f"sed: -e expression #1, char 0: no previous regular expression"
    target = resolve_path(filepath, cwd)
    node = FILESYSTEM.get(target)
    if not node:
        return f"sed: {filepath}: No such file or directory"
    try:
        _, old, new, *_ = expr.split("/")
        return node["content"].replace(old, new)
    except Exception:
        return f"sed: -e expression #1, char {len(expr)}: unterminated `s' command"


def handle_awk(args: str, cwd: str) -> str:
    """Minimal awk: just handles {print $N} pattern"""
    parts = args.strip().split(None, 1)
    if len(parts) < 2:
        return "Usage: awk [POSIX or GNU style options] -f progfile [--] file ..."
    prog = parts[0].strip("'\"")
    filepath = parts[1].strip()
    target = resolve_path(filepath, cwd)
    node = FILESYSTEM.get(target)
    if not node:
        return f"awk: can't open file {filepath}: No such file or directory"
    # Very naive: {print $1} etc
    import re
    m = re.search(r'\{print \$(\d+)\}', prog)
    if m:
        col = int(m.group(1)) - 1
        results = []
        for line in node["content"].splitlines():
            fields = line.split()
            if col < len(fields):
                results.append(fields[col])
        return "\n".join(results)
    # {print} = print all
    if "{print}" in prog:
        return node["content"]
    return ""


# ─────────────────────────────────────────────────────────────
# Main dispatcher
# ─────────────────────────────────────────────────────────────
def handle_static_command(cmd: str, cwd: str, session_history: list = None) -> tuple:
    """
    Returns (output, new_cwd, handled)

    session_history: list of command strings from the current session,
                     used for the `history` command. Pass [] if not tracking yet.
    """
    if session_history is None:
        session_history = []

    cmd = cmd.strip()
    cmd_lower = cmd.lower()

    # ── pwd ──────────────────────────────────────────────────
    if cmd == "pwd":
        return cwd, cwd, True

    # ── cd ───────────────────────────────────────────────────
    if cmd_lower.startswith("cd ") or cmd == "cd":
        args = cmd[3:] if len(cmd) > 2 else ""
        out, new_cwd = handle_cd(args, cwd)
        return out, new_cwd, True

    # ── ls ───────────────────────────────────────────────────
    if cmd == "ls" or cmd_lower.startswith("ls ") or cmd_lower.startswith("ls -"):
        args = cmd[3:] if len(cmd) > 2 else ""
        return handle_ls(args, cwd), cwd, True

    # ── cat ──────────────────────────────────────────────────
    if cmd_lower.startswith("cat "):
        return handle_cat(cmd[4:], cwd), cwd, True

    # ── tree ─────────────────────────────────────────────────
    if cmd == "tree" or cmd_lower.startswith("tree "):
        # If a path argument given, use it; otherwise use cwd
        arg = cmd[5:].strip() if len(cmd) > 4 else ""
        target = resolve_path(arg, cwd) if arg else cwd
        return handle_tree(target), cwd, True

    # ── find ─────────────────────────────────────────────────
    if cmd_lower.startswith("find"):
        return handle_find(cmd[4:].strip(), cwd), cwd, True

    # ── wc ───────────────────────────────────────────────────
    if cmd_lower.startswith("wc ") or cmd == "wc":
        return handle_wc(cmd[3:], cwd), cwd, True

    # ── history ──────────────────────────────────────────────
    if cmd == "history" or cmd_lower.startswith("history "):
        args = cmd[8:].strip() if len(cmd) > 7 else ""
        return handle_history(args, session_history), cwd, True

    # ── date ─────────────────────────────────────────────────
    if cmd == "date":
        return datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y"), cwd, True

    # ── uptime ───────────────────────────────────────────────
    if cmd == "uptime":
        return f" {datetime.datetime.now().strftime('%H:%M:%S')} up 3 days,  2:14,  1 user,  load average: 0.08, 0.12, 0.10", cwd, True

    # ── echo ─────────────────────────────────────────────────
    if cmd_lower.startswith("echo "):
        text = cmd[5:]
        env_map = {
            "$USER": "anvitha", "$HOME": "/home/anvitha",
            "$SHELL": "/bin/bash",
            "$PATH": "/home/anvitha/.local/bin:/usr/local/bin:/usr/bin:/bin",
            "$HOSTNAME": "linux", "$PWD": cwd
        }
        for k, v in env_map.items():
            text = text.replace(k, v)
        return text.strip('"').strip("'"), cwd, True

    # ── grep ─────────────────────────────────────────────────
    if cmd_lower.startswith("grep "):
        return handle_grep(cmd[5:], cwd), cwd, True

    # ── head ─────────────────────────────────────────────────
    if cmd_lower.startswith("head ") or cmd == "head":
        args = cmd[5:] if len(cmd) > 4 else ""
        return handle_head(args, cwd), cwd, True

    # ── tail ─────────────────────────────────────────────────
    if cmd_lower.startswith("tail ") or cmd == "tail":
        args = cmd[5:] if len(cmd) > 4 else ""
        return handle_tail(args, cwd), cwd, True

    # ── sed ──────────────────────────────────────────────────
    if cmd_lower.startswith("sed "):
        return handle_sed(cmd[4:], cwd), cwd, True

    # ── awk ──────────────────────────────────────────────────
    if cmd_lower.startswith("awk "):
        return handle_awk(cmd[4:], cwd), cwd, True

    # ── sudo always fails ────────────────────────────────────
    if cmd_lower.startswith("sudo") or cmd == "sudo":
        return "anvitha is not in the sudoers file. This incident will be reported.", cwd, True

    # ── apt always fails ─────────────────────────────────────
    if cmd_lower.startswith("apt"):
        return "E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)", cwd, True

    # ── fake filesystem mutations ────────────────────────────
    if cmd_lower.startswith("touch "):
        return "", cwd, True
    if cmd_lower.startswith("mkdir "):
        return "", cwd, True
    if cmd_lower.startswith("rm "):
        return "", cwd, True
    if cmd_lower.startswith("cp "):
        return "", cwd, True
    if cmd_lower.startswith("mv "):
        return "", cwd, True
    if cmd_lower.startswith("ln "):
        return "", cwd, True
    if cmd_lower.startswith("shred "):
        return "", cwd, True

    # ── chmod/chown/chgrp — deny ─────────────────────────────
    if cmd_lower.startswith("chmod "):
        return "chmod: changing permissions of: Operation not permitted", cwd, True
    if cmd_lower.startswith("chown "):
        return "chown: changing ownership of: Operation not permitted", cwd, True
    if cmd_lower.startswith("chgrp "):
        return "chgrp: changing group of: Operation not permitted", cwd, True

    # ── tar with args ────────────────────────────────────────
    if cmd_lower.startswith("tar "):
        return "tar: operation completed", cwd, True

    # ── md5sum / cksum / sum on file ─────────────────────────
    if cmd_lower.startswith("md5sum "):
        fname = cmd[7:].strip()
        return f"d41d8cd98f00b204e9800998ecf8427e  {fname}", cwd, True
    if cmd_lower.startswith("cksum "):
        fname = cmd[6:].strip()
        return f"3610880082 0 {fname}", cwd, True
    if cmd_lower.startswith("sum "):
        fname = cmd[4:].strip()
        return f"00000     0 {fname}", cwd, True

    # ── reboot / shutdown / halt / poweroff ──────────────────
    if cmd_lower in ("reboot", "shutdown", "halt", "poweroff"):
        return "Failed to set wall message, ignoring: Interactive authentication required.", cwd, True

    # ── ping with target ─────────────────────────────────────
    if cmd_lower.startswith("ping "):
        target = cmd[5:].split()[0]
        return (f"PING {target} ({target}): 56 data bytes\n"
                f"64 bytes from {target}: icmp_seq=0 ttl=64 time=0.421 ms\n"
                f"64 bytes from {target}: icmp_seq=1 ttl=64 time=0.398 ms\n"
                f"--- {target} ping statistics ---\n"
                f"2 packets transmitted, 2 received, 0% packet loss"), cwd, True

    # ── curl with URL ────────────────────────────────────────
    if cmd_lower.startswith("curl "):
        return "curl: (6) Could not resolve host: (network unreachable)", cwd, True

    # ── wget with URL ────────────────────────────────────────
    if cmd_lower.startswith("wget "):
        return "--2026-06-09 09:45:22--\nResolving host... failed: Name or service not known.\nwget: unable to resolve host address", cwd, True

    # ── ssh with target ──────────────────────────────────────
    if cmd_lower.startswith("ssh "):
        return "ssh: connect to host: Connection refused", cwd, True

    # ── scp with args ────────────────────────────────────────
    if cmd_lower.startswith("scp "):
        return "scp: Connection closed", cwd, True

    # ── kill with PID ────────────────────────────────────────
    if cmd_lower.startswith("kill "):
        parts = cmd.split()
        pid = parts[-1]
        return f"kill: ({pid}) - No such process", cwd, True

    # ── which with arg ───────────────────────────────────────
    if cmd_lower.startswith("which "):
        name = cmd[6:].strip()
        known = {"bash": "/bin/bash", "python3": "/usr/bin/python3",
                 "python": "/usr/bin/python3", "pip3": "/usr/bin/pip3",
                 "git": "/usr/bin/git", "ssh": "/usr/bin/ssh",
                 "curl": "/usr/bin/curl", "wget": "/usr/bin/wget",
                 "grep": "/usr/bin/grep", "awk": "/usr/bin/awk",
                 "sed": "/bin/sed", "vim": "/usr/bin/vim",
                 "nano": "/usr/bin/nano", "ls": "/usr/bin/ls",
                 "cat": "/usr/bin/cat", "find": "/usr/bin/find",
                 "ps": "/usr/bin/ps", "top": "/usr/bin/top"}
        return known.get(name, f"which: no {name} in ({'/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'})"), cwd, True

    # ── type with arg ────────────────────────────────────────
    if cmd_lower.startswith("type "):
        name = cmd[5:].strip()
        builtins = {"cd", "echo", "exit", "export", "alias", "pwd", "set",
                    "declare", "source", ".", "read", "return", "break",
                    "continue", "eval", "exec", "shift", "wait", "fg", "bg"}
        if name in builtins:
            return f"{name} is a shell builtin", cwd, True
        return f"{name} is /usr/bin/{name}", cwd, True

    # ── man with arg ─────────────────────────────────────────
    if cmd_lower.startswith("man "):
        name = cmd[4:].strip()
        return f"No manual entry for {name}" if name else "What manual page do you want?", cwd, True

    # ── file with arg ────────────────────────────────────────
    if cmd_lower.startswith("file "):
        path = cmd[5:].strip()
        target = resolve_path(path, cwd)
        node = FILESYSTEM.get(target)
        if not node:
            return f"file: {path}: ERROR: No such file or directory (ENOENT)", cwd, True
        if node["type"] == "dir":
            return f"{path}: directory", cwd, True
        content = node.get("content", "")
        if path.endswith(".py"):
            return f"{path}: Python script, ASCII text executable", cwd, True
        if path.endswith(".sh"):
            return f"{path}: Bourne-Again shell script, ASCII text executable", cwd, True
        if path.endswith(".pdf"):
            return f"{path}: PDF document, version 1.6", cwd, True
        if path.endswith(".gz"):
            return f"{path}: gzip compressed data, was 'tools.tar'", cwd, True
        if path.endswith(".txt"):
            return f"{path}: ASCII text", cwd, True
        return f"{path}: ASCII text", cwd, True

    # ── basename / dirname ───────────────────────────────────
    if cmd_lower.startswith("basename "):
        import os
        return os.path.basename(cmd[9:].strip()), cwd, True
    if cmd_lower.startswith("dirname "):
        import os
        return os.path.dirname(cmd[8:].strip()) or ".", cwd, True

    # ── readlink ─────────────────────────────────────────────
    if cmd_lower.startswith("readlink "):
        path = cmd[9:].strip()
        return f"readlink: {path}: No such file or directory", cwd, True

    # ── du with args ─────────────────────────────────────────
    if cmd_lower.startswith("du "):
        return "8.2G\t.", cwd, True

    # ── systemctl with args ──────────────────────────────────
    if cmd_lower.startswith("systemctl "):
        parts = cmd.split()
        if len(parts) >= 2:
            action = parts[1]
            service = parts[2] if len(parts) > 2 else "sshd"
            if action in ("start", "stop", "restart", "enable", "disable"):
                return f"Failed to {action} {service}: Interactive authentication required.", cwd, True
            if action == "status":
                return f"""● {service} - Service
   Loaded: loaded (/lib/systemd/system/{service}.service; enabled)
   Active: active (running) since Mon 2026-06-09 08:00:01 UTC; 1h 45min ago
 Main PID: 423
   CGroup: /system.slice/{service}.service""", cwd, True
        return "systemctl: missing argument", cwd, True

    # ── journalctl with args ─────────────────────────────────
    if cmd_lower.startswith("journalctl "):
        return """-- Logs begin at Mon 2026-06-09 08:00:01 UTC --
Jun 09 08:00:01 linux sshd[423]: Server listening on 0.0.0.0 port 22
Jun 09 09:12:00 linux sshd[423]: Accepted password for anvitha from 10.213.95.1 port 54231
Jun 09 09:12:01 linux sshd[423]: pam_unix(sshd:session): session opened for user anvitha""", cwd, True

    # ── git subcommands ──────────────────────────────────────
    if cmd_lower.startswith("git "):
        sub = cmd[4:].split()[0] if len(cmd) > 4 else ""
        if sub in ("status", "log", "pull", "push", "fetch", "diff", "branch", "clone"):
            return "fatal: not a git repository (or any of the parent directories): .git", cwd, True
        if sub in ("config", "init"):
            return "", cwd, True
        return f"git: '{sub}' is not a git command. See 'git --help'.", cwd, True

    # ── python3 / python with -c ─────────────────────────────
    if cmd_lower.startswith("python3 -c ") or cmd_lower.startswith("python -c "):
        return "", cwd, True  # silently execute nothing (LLM can handle interactive usage)

    # ── crontab -e / -r ──────────────────────────────────────
    if cmd_lower.startswith("crontab "):
        arg = cmd[8:].strip()
        if arg == "-l":
            return "no crontab for anvitha", cwd, True
        if arg in ("-e", "-r"):
            return "", cwd, True
        return "crontab: usage error: unrecognized option", cwd, True

    # ── sleep with arg ───────────────────────────────────────
    if cmd_lower.startswith("sleep "):
        return "", cwd, True
    if cmd == "netstat":
        return STATIC_COMMANDS["netstat -an"], cwd, True

    if cmd == "top":
        return STATIC_COMMANDS["ps aux"], cwd, True
    # ── nmap ─────────────────────────────────────────────────
    if cmd_lower.startswith("nmap"):
        return "-bash: nmap: command not found", cwd, True

    # ── look up STATIC_COMMANDS dict ─────────────────────────
    if cmd in STATIC_COMMANDS:
        return STATIC_COMMANDS[cmd], cwd, True

    # ── everything else → pass to LLM ────────────────────────
    return "", cwd, False
