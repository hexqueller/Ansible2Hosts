import sys
import re
import saver

backup_name = "/etc/hosts.backup"
host_pattern = re.compile(r'^\s*(\S+)\s+ansible_host\s*=\s*(\S+)$')

if len(sys.argv) != 2:
    print('Usage: python script.py <path_to_ansible_hosts_file>')
    sys.exit(1)

if sys.argv[1] == "restore":
    saver.restore(backup_name)
    sys.exit(1)
    
saver.backuper(backup_name)

path_to_hosts = sys.argv[1]
with open(path_to_hosts, 'r') as f:
    hosts_ansible = f.read()

hosts_list = []
for line in hosts_ansible.split('\n'):
    if line == '' or line.startswith('#'):
        continue
    match = host_pattern.match(line)
    if match:
        hostname = match.group(1)
        ip = match.group(2)
        hosts_list.append((ip, hostname))

saver.add_hosts(backup_name, hosts_list)

# for ip, hostname in hosts_list:
#     print(f'{ip}\t{hostname}') # Debug info
