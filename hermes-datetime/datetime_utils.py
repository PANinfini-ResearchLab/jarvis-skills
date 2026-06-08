#!/usr/bin/env python3
import json
from datetime import datetime, timezone
import zoneinfo

PARIS_TZ = zoneinfo.ZoneInfo("Europe/Paris")

def now_paris():
    dt = datetime.now(PARIS_TZ)
    return {
        "paris": dt.strftime("%d/%m/%Y %H:%M:%S"),
        "iso": datetime.now(timezone.utc).isoformat(),
        "offset": int(dt.utcoffset().total_seconds() / 3600),
        "is_dst": bool(dt.dst())
    }

def validate(datetime_str):
    results = {}
    # Validation native Python
    for fmt in ["%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M", "%d/%m/%Y"]:
        try:
            dt = datetime.strptime(datetime_str, fmt)
            results["french"] = {"valid": True, "format": fmt}
            break
        except:
            results["french"] = {"valid": False}
    # Validation ISO
    try:
        dt = datetime.fromisoformat(datetime_str)
        results["iso"] = {"valid": True}
    except:
        results["iso"] = {"valid": False}
    # Validation native
    try:
        dt = datetime.strptime(datetime_str, "%Y-%m-%d")
        results["native"] = {"valid": True}
    except:
        results["native"] = {"valid": False}
    valid = any(v.get("valid") for v in results.values())
    return {"input": datetime_str, "valid": valid, "validations": results}

def format_long(date=None):
    if date is None:
        date = datetime.now(PARIS_TZ)
    jours = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    mois = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    return f"{jours[date.weekday()]} {date.day} {mois[date.month-1]} {date.year}"

def relative(dt_str):
    try:
        dt = datetime.fromisoformat(dt_str).replace(tzinfo=timezone.utc)
        diff = int((datetime.now(timezone.utc) - dt).total_seconds())
        if diff < 60: return f"il y a {diff} secondes"
        if diff < 3600: return f"il y a {diff//60} minutes"
        if diff < 86400: return f"il y a {diff//3600} heures"
        return f"il y a {diff//86400} jours"
    except:
        return "date invalide"

if __name__ == "__main__":
    print(json.dumps(now_paris(), indent=2, ensure_ascii=False))
    print(json.dumps(validate("08/06/2026 14:30:00"), indent=2, ensure_ascii=False))
    print(format_long())
