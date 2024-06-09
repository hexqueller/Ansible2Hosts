import sys
import re

# Проверка наличия аргумента командной строки
if len(sys.argv) != 2:
    print('Usage: python script.py <path_to_ansible_hosts_file>')
    sys.exit(1)

# Регулярное выражение для парсинга строк файла hosts Ansible
host_pattern = re.compile(r'^\s*(\S+)\s+(.+)$')

# Чтение файла hosts Ansible
path_to_hosts = sys.argv[1]
with open(path_to_hosts, 'r') as f:
    hosts_ansible = f.read()

# Парсинг строк файла hosts Ansible
hosts_list = []
for line in hosts_ansible.split('\n'):
    if line == '' or line.startswith('#'):
        continue
    match = host_pattern.match(line)
    if match:
        ip = match.group(1)
        hostnames = match.group(2).split(' ')
        for hostname in hostnames:
            hosts_list.append((ip, hostname))

# Вывод результата в терминал в формате, подходящем для /etc/hosts
for ip, hostname in hosts_list:
    print(f'{ip}\t{hostname}')
