import sys
import re
import saver

backup_file = "/etc/hosts.backup"
host_pattern = re.compile(r'^\s*(\S+)\s+ansible_host\s*=\s*(\S+)$')

if len(sys.argv) < 2:
    print('Usage: python main.py <path_to_ansible_hosts_file1> <path_to_ansible_hosts_file2> ...')
    sys.exit(1)

if sys.argv[1] == "restore":
    saver.restore(backup_file)
    sys.exit(1)

saver.backuper(backup_file)

hosts_list = []
for path_to_hosts in sys.argv[1:]:
    try:
        with open(path_to_hosts, 'r') as f:
            hosts_ansible = f.read()
    except FileNotFoundError:
        print(f"File not found: {path_to_hosts}")
        continue

    with open(backup_file, 'r') as f:
        hosts_file = f.read()

    for line in hosts_ansible.split('\n'):
        if line == '' or line.startswith('#'):
            continue
        match = host_pattern.match(line)
        if match:
            hostname = match.group(1)
            ip = match.group(2)
            if f"{ip}\t{hostname}" not in hosts_file:
                hosts_list.append((ip, hostname))

saver.merge_files(hosts_list, sys.argv[1:], backup_file)

