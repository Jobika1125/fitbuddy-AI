"""Saving/loading data (JSON files) + small helpers."""
import json
import os
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)
PROFILE_FILE = DATA_DIR / "profile.json"
DATA_FILE = DATA_DIR / "fitbuddy_data.json"
ENV_FILE = ROOT / ".env"


def load_json(path, default):
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def save_json(path, data):
    path.write_text(json.dumps(data, indent=2))


def load_data():
    d = load_json(DATA_FILE, {})
    for k, v in (("water", {}), ("weights", []), ("workouts", [])):
        d.setdefault(k, v)
    return d


def today():
    return date.today().isoformat()


def streak(dates):
    days, d, n = set(dates), date.today(), 0
    if today() not in days:
        d -= timedelta(days=1)
    while d.isoformat() in days:
        n, d = n + 1, d - timedelta(days=1)
    return n


def saved_key():
    if os.getenv("ANTHROPIC_API_KEY"):
        return os.getenv("ANTHROPIC_API_KEY")
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                return line.split("=", 1)[1].strip().strip("\"'")
    return ""
