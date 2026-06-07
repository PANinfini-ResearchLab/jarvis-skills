import subprocess
import json

def list_jobs():
    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    return {"jobs": result.stdout}

def add_job(name, command, schedule):
    current = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    new_job = f"\n# {name}\n{schedule} {command}\n"
    updated = current + new_job
    proc = subprocess.run(["crontab", "-"], input=updated, capture_output=True, text=True)
    return {"status": f"Tâche '{name}' ajoutée : {schedule} {command}"}

def remove_job(name):
    current = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    lines = current.split('\n')
    filtered = []
    skip_next = False
    for line in lines:
        if f"# {name}" in line:
            skip_next = True
            continue
        if skip_next:
            skip_next = False
            continue
        filtered.append(line)
    updated = '\n'.join(filtered)
    subprocess.run(["crontab", "-"], input=updated, capture_output=True, text=True)
    return {"status": f"Tâche '{name}' supprimée"}

def disable_job(name):
    current = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    updated = current.replace(f"\n# {name}\n", f"\n# {name} [DISABLED]\n# ")
    subprocess.run(["crontab", "-"], input=updated, capture_output=True, text=True)
    return {"status": f"Tâche '{name}' désactivée"}

if __name__ == "__main__":
    print(json.dumps(list_jobs(), indent=2))
