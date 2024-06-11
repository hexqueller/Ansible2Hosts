import os
import shutil

def backuper(backup_file):
    if not os.path.isfile(backup_file):
        shutil.copy2("/etc/hosts", backup_file)
        print(f"Бекап создан: {backup_file}")
    else:
        pass

def add_hosts(backup_file, hosts_list):
    shutil.copy2(backup_file, "/etc/hosts")
    with open("/etc/hosts", "a") as f:
        for ip, hostname in hosts_list:
            f.write(f"{ip}\t{hostname}\n")
