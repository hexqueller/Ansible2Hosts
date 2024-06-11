import os
import shutil

def backuper(backup_file):
    if not os.path.isfile(backup_file):
        shutil.copy2("/etc/hosts", backup_file)
        print(f"Бекап создан: {backup_file}")
    else:
        pass
