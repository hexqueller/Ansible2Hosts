import os
import shutil

def backuper(backup_file):
    if not os.path.isfile(backup_file):
        shutil.copy2("/etc/hosts", backup_file)
        print(f"Backup created: {backup_file}")
    else:
        pass
        # print(f"Backup already exists: {backup_file}")

def merge_files(hosts_list, paths_to_hosts, backup_file):
    # Восстановление из бэкапа перед объединением
    restore(backup_file)
    with open("/etc/hosts", "a") as f:
        for path_to_hosts in paths_to_hosts:
            f.write(f"\n#\n# This file is merged with: {path_to_hosts}\n# The backup is located in: {backup_file}\n#\n")
        for ip, hostname in hosts_list:
            f.write(f"{ip}\t{hostname}\n")

def restore(backup_file):
    shutil.copy2(backup_file, "/etc/hosts")
    # print(f"Restored backup: {backup_file}")