"""
filesystem.py - Static fake filesystem for shelLM
Static commands = consistent attacker recon output
LLM commands = dynamic/realistic responses
Session-created files/folders (mkdir, touch, etc.) are tracked in session_fs
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
    "free -h": """               total        used        free      shared  buff/cache   available
Mem:           1.9Gi       856Mi       321Mi        12Mi       756Mi       921Mi
Swap:          2.0Gi          0B       2.0Gi""",
    "free": """               total        used        free
Mem:         2000000      876544      328704
Swap:        2097148           0     2097148""",
    "lscpu": """Architecture:            x86_64
CPU(s):                  2
Model name:              Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
CPU MHz:                 2400.000
L2 cache:                256K""",
    "dmesg": """[    0.000000] Linux version 5.15.0-91-generic
[    0.000000] BIOS-provided physical RAM map:
[    1.234567] eth0: renamed from vif1.0""",
    "sudo su": "anvitha is not in the sudoers file. This incident will be reported.",
    "sudo -l": "anvitha is not in the sudoers file. This incident will be reported.",
    "sudo apt-get update": "anvitha is not in the sudoers file. This incident will be reported.",
    "sudo apt update": "anvitha is not in the sudoers file. This incident will be reported.",
    "apt-get update": "E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)",
    "apt update": "E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)",
    "apt-get install": "E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)",
    "echo $USER": "anvitha",
    "echo $HOME": "/home/anvitha",
    "echo $SHELL": "/bin/bash",
    "echo $PATH": "/home/anvitha/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "echo $PWD": "/home/anvitha",
    "echo $HOSTNAME": "linux",
    "systemctl status": """* sshd.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled)
   Active: active (running) since Mon 2026-06-09 08:00:01 UTC""",
    "lsmod": """Module                  Size  Used by
nf_conntrack          172032  1
ip_tables              32768  1""",
    "journalctl": """-- Logs begin at Mon 2026-06-09 08:00:01 UTC --
Jun 09 08:00:01 linux sshd[423]: Server listening on 0.0.0.0 port 22
Jun 09 09:12:00 linux sshd[423]: Accepted password for anvitha""",
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
    "file": "file: missing file operand",
    "basename": "basename: missing operand",
    "dirname": "dirname: missing operand",
    "readlink": "readlink: missing operand",
    "ln": "ln: missing file operand",
    "shred": "shred: missing file operand",
    "look": "look: missing operand",
    "locate": "locate: no pattern to search for specified",
    "access": "access: missing operand",
    "tar": "tar: You must specify one of the blrRtux options",
    "gzip": "gzip: compressed data not written to a terminal.",
    "gunzip": "gunzip: compressed data not written to a terminal.",
    "zip": "Copyright (c) 1990-2008 Info-ZIP",
    "unzip": "UnZip 6.00 of 20 April 2009",
    "bzip2": "bzip2: I won't compress to a terminal.",
    "ar": "Usage: ar [emulation options] [-]{dmpqrstx}[abcDfilMNoPsSTuvV] [--plugin <name>] [member-name] [count] archive-file file...",
    "md5sum": "md5sum: missing file operand",
    "cksum": "cksum: missing file operand",
    "sum": "sum: missing file operand",
    "reboot": "Failed to set wall message, ignoring: Interactive authentication required.",
    "shutdown": "Failed to set wall message, ignoring: Interactive authentication required.",
    "halt": "Failed to set wall message, ignoring: Interactive authentication required.",
    "poweroff": "Failed to set wall message, ignoring: Interactive authentication required.",
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
    "crontab": "no crontab for anvitha",
    "crontab -l": "no crontab for anvitha",
    "atq": "",
    "batch": "",
    "ping": "ping: usage error: Destination address required",
    "curl": "curl: try 'curl --help' for more information",
    "wget": "wget: missing URL",
    "nc": "Ncat: You must specify a host to connect to. QUITTING.",
    "netcat": "usage: nc [-46CDdFhklNnrStUuvZz]",
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
     2026-06-09    52.43 MB  |   1.80 MB   |   54.23 MB  |    5.10 kbit/s""",
    "rsync": "rsync: [sender] missing source specification",
    "scp": "usage: scp [-346ABCOpqRrsTv] [-c cipher] [-D sftp_server_path] [-F ssh_config]",
    "ssh": "usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]",
    "rcp": "rcp: missing operand",
    "iwconfig": "lo        no wireless extensions.\neth0      no wireless extensions.",
    "iptables": "iptables v1.8.7 (nf_tables): no command specified",
    "ipcs": """------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status""",
    "ipcrm": "ipcrm: missing operand",
    "lshw": "-bash: lshw: command not found",
    "lsusb": "Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub",
    "hdparm": "hdparm: missing device filename",
    "dmidecode": "dmidecode: Permission denied",
    "hwclock": "2026-06-09 09:45:22.823624+00:00",
    "acpi": "Battery 0: Discharging, 85%, 02:34:12 remaining",
    "iostat": """Linux 5.15.0-91-generic (linux)   06/09/2026   _x86_64_    (2 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal  %idle
           0.42    0.00    0.21    0.08    0.00   99.29""",
    "vmstat": """procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 328704  45678 712345    0    0     3     2   45   89  0  0 99  0  0""",
    "dstat": """----total-cpu-usage---- -dsk/total- -net/total-
usr sys idl wai hiq siq| read  writ| recv  send
  0   0  99   0   0   0|  12k  5.6k|   0     0""",
    "sar": "-bash: sar: command not found",
    "mpstat": """Linux 5.15.0-91-generic (linux)   06/09/2026   _x86_64_    (2 CPU)

09:45:21 AM  CPU    %usr   %nice    %sys %iowait    %idle
09:45:21 AM  all    0.42    0.00    0.21    0.08   99.29""",
    "pidof": "pidof: usage error: no program name specified",
    "pmap": "pmap: missing operand",
    "strace": "strace: must have PROG [ARGS] or -p PID",
    "watch": "watch: missing operand",
    "kill": "kill: usage: kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]",
    "bg": "bash: bg: no job control",
    "fg": "bash: fg: no job control",
    "chrt": "chrt: missing argument",
    "fdisk": "fdisk: cannot open /dev/sda: Permission denied",
    "cfdisk": "cfdisk: cannot open /dev/sda: Permission denied",
    "sync": "",
    "dosfsck": "dosfsck: missing device",
    "dump": "-bash: dump: command not found",
    "restore": "-bash: restore: command not found",
    "dumpe2fs": "dumpe2fs: Permission denied while trying to open /dev/sda1",
    "alias": "alias ll='ls -alF'\nalias la='ls -A'\nalias l='ls -CF'\nalias gs='git status'\nalias gp='git pull'",
    "export": "declare -x EDITOR=\"vim\"\ndeclare -x HOME=\"/home/anvitha\"\ndeclare -x LOGNAME=\"anvitha\"\ndeclare -x PATH=\"/home/anvitha/.local/bin:/usr/local/bin:/usr/bin:/bin\"\ndeclare -x SHELL=\"/bin/bash\"\ndeclare -x USER=\"anvitha\"",
    "env": "SHELL=/bin/bash\nUSER=anvitha\nHOME=/home/anvitha\nPATH=/home/anvitha/.local/bin:/usr/local/bin:/usr/bin:/bin\nEDITOR=vim\nLANG=en_US.UTF-8",
    "printenv": "SHELL=/bin/bash\nUSER=anvitha\nHOME=/home/anvitha\nPATH=/home/anvitha/.local/bin:/usr/local/bin:/usr/bin:/bin\nEDITOR=vim\nLANG=en_US.UTF-8",
    "set": "BASH=/bin/bash\nHOME=/home/anvitha\nHOSTNAME=linux\nSHELL=/bin/bash\nUSER=anvitha",
    "declare": "",
    "type": "type: usage: type [-afptP] name [name ...]",
    "which": "which: no argument given",
    "exit": "",
    "cal": datetime.datetime.now().strftime("""    %B %Y
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30"""),
    "wall": "",
    "write": "write: write: you have write permission turned off.",
    "mailq": "Mail queue is empty",
    "biff": "biff: not currently receiving mail",
    "eject": "eject: unable to eject, last error: Operation not permitted",
    "cupsd": "cupsd: Permission denied",
    "script": "Script started, file is typescript",
    "scriptreplay": "scriptreplay: missing argument",
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
    "service": "Usage: service < option > | --status-all | [ service_name [ command | --full-restart ] ]",
    "admin": "anvitha",
    "administrator": "anvitha",
    "root": "anvitha",
    "nc -zv": "Ncat: Connection refused.",
    "telnet": "telnet: command not found",
    "ftp": "ftp: command not found",
}


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Session filesystem helpers
# session_fs structure: { "dirs": set([...full paths...]), "files": {full_path: content} }
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def _ensure_session_fs(session_fs):
    if session_fs is None:
        session_fs = {"dirs": set(), "files": {}}
    if "dirs" not in session_fs:
        session_fs["dirs"] = set()
    if "files" not in session_fs:
        session_fs["files"] = {}
    return session_fs


def path_exists(path, session_fs):
    """Check if path exists in base FILESYSTEM or session_fs."""
    if path in FILESYSTEM:
        return True
    if path in session_fs["dirs"]:
        return True
    if path in session_fs["files"]:
        return True
    return False


def is_dir(path, session_fs):
    if path in FILESYSTEM:
        return FILESYSTEM[path]["type"] == "dir"
    if path in session_fs["dirs"]:
        return True
    if path in session_fs["files"]:
        return False
    return False


def get_contents(path, session_fs):
    """List contents of a directory, merging base FILESYSTEM and session_fs."""
    items = []
    if path in FILESYSTEM and FILESYSTEM[path]["type"] == "dir":
        items.extend(FILESYSTEM[path]["contents"])

    prefix = path.rstrip("/") + "/"
    seen = set(items)

    # session-created dirs directly under this path
    for d in session_fs["dirs"]:
        if d.startswith(prefix):
            rel = d[len(prefix):]
            if "/" not in rel and rel and rel not in seen:
                items.append(rel)
                seen.add(rel)

    # session-created files directly under this path
    for f in session_fs["files"]:
        if f.startswith(prefix):
            rel = f[len(prefix):]
            if "/" not in rel and rel and rel not in seen:
                items.append(rel)
                seen.add(rel)

    return items


def get_file_content(path, session_fs):
    if path in session_fs["files"]:
        return session_fs["files"][path]
    if path in FILESYSTEM and FILESYSTEM[path]["type"] == "file":
        return FILESYSTEM[path]["content"]
    return None


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Helper: resolve path
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
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


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# ls
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_ls(args: str, cwd: str, session_fs) -> str:
    target = cwd
    show_hidden = "-a" in args or "-la" in args or "-al" in args
    long_format = "-l" in args
    parts = args.split()
    for p in parts:
        if not p.startswith("-"):
            target = resolve_path(p, cwd)
            break

    if not path_exists(target, session_fs):
        return f"ls: cannot access '{target}': No such file or directory"

    if not is_dir(target, session_fs):
        return target

    all_items = get_contents(target, session_fs)
    if show_hidden:
        items = [".", ".."] + all_items
    else:
        items = [i for i in all_items if not i.startswith(".")]

    if long_format:
        lines = ["total " + str(len(items) * 4)]
        for item in items:
            full = target.rstrip("/") + "/" + item
            isd = is_dir(full, session_fs)
            perm = "drwxr-xr-x" if isd else "-rw-r--r--"
            content = get_file_content(full, session_fs) or ""
            size = "4096" if isd else str(len(content))
            lines.append(f"{perm} 2 anvitha anvitha {size:>6} Jun  4 09:12 {item}")
        return "\n".join(lines)
    return "  ".join(items)


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# cat
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_cat(args: str, cwd: str, session_fs) -> str:
    path = args.strip()
    if not path:
        return ""
    target = resolve_path(path, cwd)
    if not path_exists(target, session_fs):
        return f"cat: {path}: No such file or directory"
    if is_dir(target, session_fs):
        return f"cat: {path}: Is a directory"
    return get_file_content(target, session_fs) or ""


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# cd
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_cd(args: str, cwd: str, session_fs) -> tuple:
    target = args.strip()
    if not target or target == "~":
        return "", "/home/anvitha"
    new_path = resolve_path(target, cwd)
    if not path_exists(new_path, session_fs):
        return f"bash: cd: {target}: No such file or directory", cwd
    if not is_dir(new_path, session_fs):
        return f"bash: cd: {target}: Not a directory", cwd
    return "", new_path


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# tree
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_tree(cwd: str, session_fs) -> str:
    if not path_exists(cwd, session_fs) or not is_dir(cwd, session_fs):
        return f"tree: '{cwd}': No such file or directory"

    lines = ["."]
    dir_count = [0]
    file_count = [0]

    def _recurse(path: str, prefix: str):
        items = get_contents(path, session_fs)
        for i, item in enumerate(items):
            is_last = (i == len(items) - 1)
            connector = "+-- "
            child_path = path.rstrip("/") + "/" + item
            child_is_dir = is_dir(child_path, session_fs)
            lines.append(prefix + connector + item)
            if child_is_dir:
                dir_count[0] += 1
                extension = "    " if is_last else "|   "
                _recurse(child_path, prefix + extension)
            else:
                file_count[0] += 1

    _recurse(cwd, "")
    lines.append("")
    lines.append(f"{dir_count[0]} directories, {file_count[0]} files")
    return "\n".join(lines)


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# find
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_find(args: str, cwd: str, session_fs) -> str:
    results = []
    for path in FILESYSTEM:
        if path.startswith(cwd):
            results.append(path)
    for path in session_fs["dirs"]:
        if path.startswith(cwd):
            results.append(path)
    for path in session_fs["files"]:
        if path.startswith(cwd):
            results.append(path)
    return "\n".join(sorted(set(results))) if results else ""


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# wc
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_wc(args: str, cwd: str, session_fs) -> str:
    path = args.strip().split()[-1] if args.strip() else ""
    if not path:
        return "wc: missing file operand"
    target = resolve_path(path, cwd)
    content = get_file_content(target, session_fs)
    if content is None:
        return f"wc: {path}: No such file or directory"
    lines = content.count("\n") + 1
    words = len(content.split())
    chars = len(content)
    return f" {lines} {words} {chars} {path}"


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# history
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_history(args: str, session_history: list) -> str:
    if not session_history:
        return ""
    limit = None
    try:
        n = int(args.strip())
        limit = n
    except (ValueError, TypeError):
        pass

    entries = session_history if limit is None else session_history[-limit:]
    offset = len(session_history) - len(entries) + 1
    lines = []
    for i, cmd in enumerate(entries, start=offset):
        lines.append(f"  {i:4d}  {cmd}")
    return "\n".join(lines)


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# grep / head / tail / sed / awk
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_grep(args: str, cwd: str, session_fs) -> str:
    parts = args.strip().split(None, 1)
    if len(parts) < 2:
        return "Usage: grep [OPTION]... PATTERN [FILE]..."
    pattern, filepath = parts[0], parts[1].strip()
    target = resolve_path(filepath, cwd)
    content = get_file_content(target, session_fs)
    if content is None:
        if is_dir(target, session_fs):
            return f"grep: {filepath}: Is a directory"
        return f"grep: {filepath}: No such file or directory"
    matches = [line for line in content.splitlines() if pattern.lower() in line.lower()]
    return "\n".join(matches)


def handle_head(args: str, cwd: str, session_fs) -> str:
    parts = args.strip().split()
    n = 10
    filepath = ""
    i = 0
    while i < len(parts):
        if parts[i] == "-n" and i + 1 < len(parts):
            try:
                n = int(parts[i + 1]); i += 2; continue
            except ValueError:
                pass
        elif parts[i].startswith("-") and len(parts[i]) > 1:
            try:
                n = int(parts[i][1:]); i += 1; continue
            except ValueError:
                pass
        else:
            filepath = parts[i]
        i += 1
    if not filepath:
        return "head: missing file operand"
    target = resolve_path(filepath, cwd)
    content = get_file_content(target, session_fs)
    if content is None:
        return f"head: cannot open '{filepath}' for reading: No such file or directory"
    lines = content.splitlines()
    return "\n".join(lines[:n])


def handle_tail(args: str, cwd: str, session_fs) -> str:
    parts = args.strip().split()
    n = 10
    filepath = ""
    i = 0
    while i < len(parts):
        if parts[i] == "-n" and i + 1 < len(parts):
            try:
                n = int(parts[i + 1]); i += 2; continue
            except ValueError:
                pass
        elif parts[i].startswith("-") and len(parts[i]) > 1:
            try:
                n = int(parts[i][1:]); i += 1; continue
            except ValueError:
                pass
        else:
            filepath = parts[i]
        i += 1
    if not filepath:
        return "tail: missing file operand"
    target = resolve_path(filepath, cwd)
    content = get_file_content(target, session_fs)
    if content is None:
        return f"tail: cannot open '{filepath}' for reading: No such file or directory"
    lines = content.splitlines()
    return "\n".join(lines[-n:])


def handle_sed(args: str, cwd: str, session_fs) -> str:
    parts = args.strip().split(None, 1)
    if len(parts) < 2:
        return "Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]..."
    expr = parts[0]
    filepath = parts[1].strip()
    if not expr.startswith("s/"):
        return "sed: -e expression #1, char 0: no previous regular expression"
    target = resolve_path(filepath, cwd)
    content = get_file_content(target, session_fs)
    if content is None:
        return f"sed: {filepath}: No such file or directory"
    try:
        _, old, new, *_ = expr.split("/")
        return content.replace(old, new)
    except Exception:
        return f"sed: -e expression #1, char {len(expr)}: unterminated `s' command"


def handle_awk(args: str, cwd: str, session_fs) -> str:
    parts = args.strip().split(None, 1)
    if len(parts) < 2:
        return "Usage: awk [POSIX or GNU style options] -f progfile [--] file ..."
    prog = parts[0].strip("'\"")
    filepath = parts[1].strip()
    target = resolve_path(filepath, cwd)
    content = get_file_content(target, session_fs)
    if content is None:
        return f"awk: can't open file {filepath}: No such file or directory"
    import re
    m = re.search(r'\{print \$(\d+)\}', prog)
    if m:
        col = int(m.group(1)) - 1
        results = []
        for line in content.splitlines():
            fields = line.split()
            if col < len(fields):
                results.append(fields[col])
        return "\n".join(results)
    if "{print}" in prog:
        return content
    return ""


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Main dispatcher
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def handle_static_command(cmd: str, cwd: str, session_history: list = None, session_fs=None) -> tuple:
    """
    Returns (output, new_cwd, handled)

    session_history: list of command strings from current session (for `history`)
    session_fs: dict with "dirs" (set of paths) and "files" (path->content),
                tracks mkdir/touch/rm/cp/mv/echo > created during the session.
                Pass the SAME dict object every call so it persists.
    """
    if session_history is None:
        session_history = []
    session_fs = _ensure_session_fs(session_fs)

    cmd = cmd.strip()
    cmd_lower = cmd.lower()

    # â”€â”€ pwd â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd == "pwd":
        return cwd, cwd, True

    # â”€â”€ cd â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("cd ") or cmd == "cd":
        args = cmd[3:] if len(cmd) > 2 else ""
        out, new_cwd = handle_cd(args, cwd, session_fs)
        return out, new_cwd, True

    # â”€â”€ ls â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd == "ls" or cmd_lower.startswith("ls ") or cmd_lower.startswith("ls -"):
        args = cmd[3:] if len(cmd) > 2 else ""
        return handle_ls(args, cwd, session_fs), cwd, True

    # â”€â”€ cat â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("cat "):
        return handle_cat(cmd[4:], cwd, session_fs), cwd, True

    # â”€â”€ tree â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd == "tree" or cmd_lower.startswith("tree "):
        arg = cmd[5:].strip() if len(cmd) > 4 else ""
        target = resolve_path(arg, cwd) if arg else cwd
        return handle_tree(target, session_fs), cwd, True

    # â”€â”€ find â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("find"):
        return handle_find(cmd[4:].strip(), cwd, session_fs), cwd, True

    # â”€â”€ wc â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("wc ") or cmd == "wc":
        return handle_wc(cmd[3:], cwd, session_fs), cwd, True

    # â”€â”€ history â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd == "history" or cmd_lower.startswith("history "):
        args = cmd[8:].strip() if len(cmd) > 7 else ""
        return handle_history(args, session_history), cwd, True

    # â”€â”€ date â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd == "date":
        return datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y"), cwd, True

    # â”€â”€ uptime â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd == "uptime":
        return f" {datetime.datetime.now().strftime('%H:%M:%S')} up 3 days,  2:14,  1 user,  load average: 0.08, 0.12, 0.10", cwd, True

    # â”€â”€ echo (with redirection support) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("echo "):
        rest = cmd[5:]
        # handle echo "text" > file  or  >> file
        if ">>" in rest or ">" in rest:
            append = ">>" in rest
            sep = ">>" if append else ">"
            text_part, file_part = rest.split(sep, 1)
            text = text_part.strip().strip('"').strip("'")
            filepath = file_part.strip()
            target = resolve_path(filepath, cwd)
            if append:
                existing = get_file_content(target, session_fs) or ""
                session_fs["files"][target] = (existing + "\n" + text) if existing else text
            else:
                session_fs["files"][target] = text
            # remove from dirs if it was one (overwritten as file)
            session_fs["dirs"].discard(target)
            return "", cwd, True

        text = rest
        env_map = {
            "$USER": "anvitha", "$HOME": "/home/anvitha",
            "$SHELL": "/bin/bash",
            "$PATH": "/home/anvitha/.local/bin:/usr/local/bin:/usr/bin:/bin",
            "$HOSTNAME": "linux", "$PWD": cwd
        }
        for k, v in env_map.items():
            text = text.replace(k, v)
        return text.strip('"').strip("'"), cwd, True

    # â”€â”€ grep â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("grep "):
        return handle_grep(cmd[5:], cwd, session_fs), cwd, True

    # â”€â”€ head â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("head ") or cmd == "head":
        args = cmd[5:] if len(cmd) > 4 else ""
        return handle_head(args, cwd, session_fs), cwd, True

    # â”€â”€ tail â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("tail ") or cmd == "tail":
        args = cmd[5:] if len(cmd) > 4 else ""
        return handle_tail(args, cwd, session_fs), cwd, True

    # â”€â”€ sed â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("sed "):
        return handle_sed(cmd[4:], cwd, session_fs), cwd, True

    # â”€â”€ awk â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("awk "):
        return handle_awk(cmd[4:], cwd, session_fs), cwd, True

    # â”€â”€ sudo always fails â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("sudo") or cmd == "sudo":
        return "anvitha is not in the sudoers file. This incident will be reported.", cwd, True

    # â”€â”€ apt always fails â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("apt"):
        return "E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)", cwd, True

    # â”€â”€ mkdir â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("mkdir "):
        args = cmd[6:].strip()
        make_parents = False
        names = []
        for a in args.split():
            if a in ("-p", "-pv", "-vp"):
                make_parents = True
            else:
                names.append(a)
        if not names:
            return "mkdir: missing operand", cwd, True
        errors = []
        for name in names:
            target = resolve_path(name, cwd)
            if path_exists(target, session_fs):
                errors.append(f"mkdir: cannot create directory '{name}': File exists")
                continue
            parent = "/".join(target.rstrip("/").split("/")[:-1]) or "/"
            if not make_parents and not path_exists(parent, session_fs):
                errors.append(f"mkdir: cannot create directory '{name}': No such file or directory")
                continue
            # create parents if -p
            if make_parents:
                parts = target.strip("/").split("/")
                cur = ""
                for part in parts[:-1]:
                    cur += "/" + part
                    if not path_exists(cur, session_fs):
                        session_fs["dirs"].add(cur)
            session_fs["dirs"].add(target)
        return "\n".join(errors), cwd, True

    # â”€â”€ touch â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("touch "):
        names = cmd[6:].strip().split()
        for name in names:
            target = resolve_path(name, cwd)
            if not path_exists(target, session_fs):
                session_fs["files"][target] = ""
        return "", cwd, True

    # â”€â”€ rm â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("rm "):
        args = cmd[3:].strip()
        recursive = False
        names = []
        for a in args.split():
            if a in ("-r", "-rf", "-fr", "-f", "-rv", "-vr"):
                if "r" in a:
                    recursive = True
            else:
                names.append(a)
        errors = []
        for name in names:
            target = resolve_path(name, cwd)
            if not path_exists(target, session_fs):
                errors.append(f"rm: cannot remove '{name}': No such file or directory")
                continue
            if is_dir(target, session_fs) and not recursive:
                errors.append(f"rm: cannot remove '{name}': Is a directory")
                continue
            if is_dir(target, session_fs):
                # remove dir and everything under it (only session-created)
                prefix = target.rstrip("/") + "/"
                session_fs["dirs"] = {d for d in session_fs["dirs"] if not (d == target or d.startswith(prefix))}
                session_fs["files"] = {f: c for f, c in session_fs["files"].items() if not f.startswith(prefix)}
            else:
                session_fs["files"].pop(target, None)
        return "\n".join(errors), cwd, True

    # â”€â”€ rmdir â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("rmdir "):
        name = cmd[6:].strip()
        target = resolve_path(name, cwd)
        if not path_exists(target, session_fs):
            return f"rmdir: failed to remove '{name}': No such file or directory", cwd, True
        if not is_dir(target, session_fs):
            return f"rmdir: failed to remove '{name}': Not a directory", cwd, True
        if get_contents(target, session_fs):
            return f"rmdir: failed to remove '{name}': Directory not empty", cwd, True
        session_fs["dirs"].discard(target)
        return "", cwd, True

    # â”€â”€ cp â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("cp "):
        parts = cmd[3:].strip().split()
        parts = [p for p in parts if not p.startswith("-")]
        if len(parts) < 2:
            return "cp: missing destination file operand", cwd, True
        src, dst = parts[0], parts[1]
        src_t = resolve_path(src, cwd)
        dst_t = resolve_path(dst, cwd)
        content = get_file_content(src_t, session_fs)
        if content is None:
            if is_dir(src_t, session_fs):
                return f"cp: -r not specified; omitting directory '{src}'", cwd, True
            return f"cp: cannot stat '{src}': No such file or directory", cwd, True
        if is_dir(dst_t, session_fs):
            fname = src_t.rstrip("/").split("/")[-1]
            dst_t = dst_t.rstrip("/") + "/" + fname
        session_fs["files"][dst_t] = content
        return "", cwd, True

    # â”€â”€ mv â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("mv "):
        parts = cmd[3:].strip().split()
        if len(parts) < 2:
            return "mv: missing destination file operand", cwd, True
        src, dst = parts[0], parts[1]
        src_t = resolve_path(src, cwd)
        dst_t = resolve_path(dst, cwd)
        if not path_exists(src_t, session_fs):
            return f"mv: cannot stat '{src}': No such file or directory", cwd, True
        if is_dir(dst_t, session_fs):
            fname = src_t.rstrip("/").split("/")[-1]
            dst_t = dst_t.rstrip("/") + "/" + fname
        if is_dir(src_t, session_fs):
            # move dir (only session-created dirs can truly be moved)
            session_fs["dirs"].discard(src_t)
            session_fs["dirs"].add(dst_t)
            prefix = src_t.rstrip("/") + "/"
            new_prefix = dst_t.rstrip("/") + "/"
            for f in list(session_fs["files"]):
                if f.startswith(prefix):
                    session_fs["files"][new_prefix + f[len(prefix):]] = session_fs["files"].pop(f)
            for d in list(session_fs["dirs"]):
                if d.startswith(prefix):
                    session_fs["dirs"].discard(d)
                    session_fs["dirs"].add(new_prefix + d[len(prefix):])
        else:
            content = get_file_content(src_t, session_fs) or ""
            session_fs["files"][dst_t] = content
            session_fs["files"].pop(src_t, None)
        return "", cwd, True

    # â”€â”€ ln â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("ln "):
        return "", cwd, True

    # â”€â”€ shred â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("shred "):
        return "", cwd, True

    # â”€â”€ chmod/chown/chgrp â€” deny â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("chmod "):
        return "chmod: changing permissions of: Operation not permitted", cwd, True
    if cmd_lower.startswith("chown "):
        return "chown: changing ownership of: Operation not permitted", cwd, True
    if cmd_lower.startswith("chgrp "):
        return "chgrp: changing group of: Operation not permitted", cwd, True

    # â”€â”€ tar with args â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("tar "):
        return "tar: operation completed", cwd, True

    # â”€â”€ md5sum / cksum / sum on file â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("md5sum "):
        fname = cmd[7:].strip()
        return f"d41d8cd98f00b204e9800998ecf8427e  {fname}", cwd, True
    if cmd_lower.startswith("cksum "):
        fname = cmd[6:].strip()
        return f"3610880082 0 {fname}", cwd, True
    if cmd_lower.startswith("sum "):
        fname = cmd[4:].strip()
        return f"00000     0 {fname}", cwd, True

    # â”€â”€ reboot / shutdown / halt / poweroff â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower in ("reboot", "shutdown", "halt", "poweroff"):
        return "Failed to set wall message, ignoring: Interactive authentication required.", cwd, True

    # â”€â”€ ping with target â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("ping "):
        target = cmd[5:].split()[0]
        return (f"PING {target} ({target}): 56 data bytes\n"
                f"64 bytes from {target}: icmp_seq=0 ttl=64 time=0.421 ms\n"
                f"64 bytes from {target}: icmp_seq=1 ttl=64 time=0.398 ms\n"
                f"--- {target} ping statistics ---\n"
                f"2 packets transmitted, 2 received, 0% packet loss"), cwd, True

    # â”€â”€ curl with URL â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("curl "):
        return "curl: (6) Could not resolve host: (network unreachable)", cwd, True

    # â”€â”€ wget with URL â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("wget "):
        return "--2026-06-09 09:45:22--\nResolving host... failed: Name or service not known.\nwget: unable to resolve host address", cwd, True

    # â”€â”€ ssh with target â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("ssh "):
        return "ssh: connect to host: Connection refused", cwd, True

    # â”€â”€ scp with args â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("scp "):
        return "scp: Connection closed", cwd, True

    # â”€â”€ nc/netcat with args â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("nc ") or cmd_lower.startswith("netcat "):
        return "Ncat: Connection refused.", cwd, True

    # â”€â”€ kill with PID â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("kill "):
        pid = cmd.split()[-1]
        return f"kill: ({pid}) - No such process", cwd, True

    # â”€â”€ which with arg â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
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
        return known.get(name, f"which: no {name} in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin)"), cwd, True

    # â”€â”€ type with arg â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("type "):
        name = cmd[5:].strip()
        builtins = {"cd", "echo", "exit", "export", "alias", "pwd", "set",
                    "declare", "source", ".", "read", "return", "break",
                    "continue", "eval", "exec", "shift", "wait", "fg", "bg"}
        if name in builtins:
            return f"{name} is a shell builtin", cwd, True
        return f"{name} is /usr/bin/{name}", cwd, True

    # â”€â”€ man with arg â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("man "):
        name = cmd[4:].strip()
        return f"No manual entry for {name}" if name else "What manual page do you want?", cwd, True

    # â”€â”€ file with arg â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("file "):
        path = cmd[5:].strip()
        target = resolve_path(path, cwd)
        if not path_exists(target, session_fs):
            return f"file: {path}: ERROR: No such file or directory (ENOENT)", cwd, True
        if is_dir(target, session_fs):
            return f"{path}: directory", cwd, True
        if path.endswith(".py"):
            return f"{path}: Python script, ASCII text executable", cwd, True
        if path.endswith(".sh"):
            return f"{path}: Bourne-Again shell script, ASCII text executable", cwd, True
        if path.endswith(".pdf"):
            return f"{path}: PDF document, version 1.6", cwd, True
        if path.endswith(".gz"):
            return f"{path}: gzip compressed data, was 'tools.tar'", cwd, True
        return f"{path}: ASCII text", cwd, True

    # â”€â”€ basename / dirname â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("basename "):
        import os
        return os.path.basename(cmd[9:].strip()), cwd, True
    if cmd_lower.startswith("dirname "):
        import os
        return os.path.dirname(cmd[8:].strip()) or ".", cwd, True

    # â”€â”€ readlink â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("readlink "):
        path = cmd[9:].strip()
        return f"readlink: {path}: No such file or directory", cwd, True

    # â”€â”€ du with args â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("du "):
        return "8.2G\t.", cwd, True

    # â”€â”€ netstat / top (alias to static dict) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd == "netstat":
        return STATIC_COMMANDS["netstat -an"], cwd, True

    if cmd == "top":
        return STATIC_COMMANDS["ps aux"], cwd, True

    # â”€â”€ systemctl with args â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("systemctl "):
        parts = cmd.split()
        if len(parts) >= 2:
            action = parts[1]
            service = parts[2] if len(parts) > 2 else "sshd"
            if action in ("start", "stop", "restart", "enable", "disable"):
                return f"Failed to {action} {service}: Interactive authentication required.", cwd, True
            if action == "status":
                return f"""* {service} - Service
   Loaded: loaded (/lib/systemd/system/{service}.service; enabled)
   Active: active (running) since Mon 2026-06-09 08:00:01 UTC; 1h 45min ago
 Main PID: 423""", cwd, True
        return "systemctl: missing argument", cwd, True

    # â”€â”€ journalctl with args â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("journalctl "):
        return """-- Logs begin at Mon 2026-06-09 08:00:01 UTC --
Jun 09 08:00:01 linux sshd[423]: Server listening on 0.0.0.0 port 22
Jun 09 09:12:00 linux sshd[423]: Accepted password for anvitha from 10.213.95.1 port 54231
Jun 09 09:12:01 linux sshd[423]: pam_unix(sshd:session): session opened for user anvitha""", cwd, True

    # â”€â”€ git subcommands â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("git "):
        sub = cmd[4:].split()[0] if len(cmd) > 4 else ""
        if sub in ("status", "log", "pull", "push", "fetch", "diff", "branch", "clone"):
            return "fatal: not a git repository (or any of the parent directories): .git", cwd, True
        if sub in ("config", "init"):
            return "", cwd, True
        return f"git: '{sub}' is not a git command. See 'git --help'.", cwd, True

    # â”€â”€ python3 / python with -c â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("python3 -c ") or cmd_lower.startswith("python -c "):
        return "", cwd, True

    # â”€â”€ crontab -e / -r â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("crontab "):
        arg = cmd[8:].strip()
        if arg == "-l":
            return "no crontab for anvitha", cwd, True
        if arg in ("-e", "-r"):
            return "", cwd, True
        return "crontab: usage error: unrecognized option", cwd, True

    # â”€â”€ sleep with arg â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower.startswith("sleep "):
        return "", cwd, True

    # â”€â”€ nmap â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # â”€â”€ custom firewall status â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd_lower == "show firewall status":
        return """[OK] Firewalld service is running
Active firewall zone: default
Firewall enabled: yes
Firewall active: yes""", cwd, True

# â”€â”€ look up STATIC_COMMANDS dict â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    if cmd == "htop" or cmd == "top":
        return """top - 18:54:49 up 3 days,  2:14,  1 user,  load average: 0.08, 0.12, 0.10
Tasks:  89 total,   1 running,  88 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.4 us,  0.2 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.1 si
MiB Mem :   1953.6 total,    321.4 free,    856.2 used,    776.0 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.    921.4 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0  168548   9876   6432 S   0.0   0.5   0:02.34 init
  423 root      20   0   15420   2048   1024 S   0.0   0.1   0:00.12 sshd
  891 postgres  20   0  214356  18432  12288 S   0.0   0.9   0:01.23 postgres
 1203 anvitha   20   0  612480  24576  18432 S   0.0   1.2   0:03.45 python3
 1204 anvitha   20   0   21456   8192   4096 S   0.0   0.4   0:00.00 bash""", cwd, True
    if cmd_lower.startswith("service "):
        parts = cmd.split()
        service = parts[1] if len(parts) > 1 else "ssh"
        action = parts[2] if len(parts) > 2 else "status"
        if action == "status":
            return f" * {service} is running\n * {service} start/running, process 423", cwd, True
        if action in ("start", "stop", "restart"):
            return f"{service}: unrecognized service", cwd, True
        return f"Usage: service {service} start|stop|restart|status", cwd, True

    if cmd_lower.startswith("nmap"):
        return "-bash: nmap: command not found", cwd, True
    if cmd in STATIC_COMMANDS:
        return STATIC_COMMANDS[cmd], cwd, True


