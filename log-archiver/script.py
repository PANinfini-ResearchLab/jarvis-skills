import subprocess
import json
import os
import time
import tarfile
from datetime import datetime

ARCHIVE_DIR = "/mnt/JARVIS-SSD/logs/archives"

def archive_logs(days=30):
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    now = time.time()
    threshold = now - (days * 24 * 60 * 60)
    archived = []
    archive_name = f"{ARCHIVE_DIR}/logs_{datetime.now().strftime('%Y-%m-%d')}.tar.gz"
    with tarfile.open(archive_name, "w:gz") as tar:
        for log_dir in ["/var/log", os.path.expanduser("~/.hermes/logs")]:
            if os.path.exists(log_dir):
                for root, dirs, files in os.walk(log_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if os.path.getmtime(file_path) < threshold:
                            tar.add(file_path)
                            archived.append(file_path)
    return {"archive": archive_name, "archived_files": archived, "count": len(archived)}

def compress_logs(path):
    compressed = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                subprocess.run(["gzip", file_path])
                compressed.append(file_path)
    return {"compressed": compressed}

def delete_old_archives(days=90):
    now = time.time()
    threshold = now - (days * 24 * 60 * 60)
    deleted = []
    if os.path.exists(ARCHIVE_DIR):
        for file in os.listdir(ARCHIVE_DIR):
            file_path = os.path.join(ARCHIVE_DIR, file)
            if os.path.getmtime(file_path) < threshold:
                os.remove(file_path)
                deleted.append(file_path)
    return {"deleted": deleted, "count": len(deleted)}

def list_archives():
    if not os.path.exists(ARCHIVE_DIR):
        return {"archives": []}
    archives = []
    for file in os.listdir(ARCHIVE_DIR):
        file_path = os.path.join(ARCHIVE_DIR, file)
        archives.append({"file": file, "size_mb": round(os.path.getsize(file_path) / (1024*1024), 2)})
    return {"archives": archives}

def restore_archive(archive):
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall("/")
    return {"status": f"Archive {archive} restaurée"}

if __name__ == "__main__":
    print(json.dumps(list_archives(), indent=2))
