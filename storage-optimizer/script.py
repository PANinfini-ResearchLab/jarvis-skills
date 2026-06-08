import subprocess
import json
import os
import time

def check_storage():
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    return {"storage_usage": result.stdout}

def clean_old_files(path, days):
    now = time.time()
    threshold = now - (days * 24 * 60 * 60)
    deleted = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) < threshold:
                os.remove(file_path)
                deleted.append(file_path)
    return {"deleted_files": deleted, "count": len(deleted)}

def find_large_files(path, size_mb):
    large_files = []
    size_bytes = size_mb * 1024 * 1024
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                if size > size_bytes:
                    large_files.append({"path": file_path, "size_mb": round(size / (1024*1024), 2)})
            except:
                pass
    return {"large_files": large_files}

def compress_logs(path):
    compressed = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                subprocess.run(["gzip", file_path])
                compressed.append(file_path)
    return {"compressed": compressed}

def defrag_raid():
    result = subprocess.run(["cat", "/proc/mdstat"], capture_output=True, text=True)
    return {"raid_status": result.stdout}

def move_to_nas(source, destination):
    os.makedirs(destination, exist_ok=True)
    subprocess.run(["mv", source, destination])
    return {"status": f"Déplacé {source} vers {destination}"}

if __name__ == "__main__":
    print(json.dumps(check_storage(), indent=2))
