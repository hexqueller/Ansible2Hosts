import sys
import re
import saver

if len(sys.argv) != 2:
    print('Usage: python script.py <path_to_ansible_hosts_file>')
    sys.exit(1)

host_pattern = re.compile(r'^\s*(\S+)\s+ansible_host\s*=\s*(\S+)$')

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

for ip, hostname in hosts_list:
    print(f'{ip}\t{hostname}')

saver.backuper("/etc/hosts.backup")
