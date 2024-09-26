# Ansible2Hosts

Конвертер файлов hosts из формата Ansible в формат Linux

## Описание
 Ansible2Hosts - это простая утилита, которая позволяет легко конвертировать файлы hosts, созданные для использования с Ansible, в формат, понятный системе Linux.

## Использование
### Запуск программы
`sudo python main.py <path_to_ansible_hosts_file> <another_file> ...`

### Восстановление
`sudo python main.py restore`

### Пример
Если у вас есть файл `hosts` в формате Ansible со следующим содержимым:
```bash
server1 ansible_host=192.168.1.100
server2 ansible_host=192.168.1.101
```
Вы можете запустить программу, указав путь к этому файлу:
python main.py /path/to/hosts
Программа запишет в файл /etc/hosts:
```bash
192.168.1.100 server1
192.168.1.101 server2
```
