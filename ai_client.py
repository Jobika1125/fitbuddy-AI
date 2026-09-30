"""Claude API client (plain urllib, no extra packages)."""
import json
import urllib.error
import urllib.request

from .calculator import calc_targets
from .config import API_URL, MODEL
from .storage import streak, today


def ask_claude(key, profile, data, history):
    _, _, _, target = calc_targets(profile)
    ctx = {**profile, "target_kcal": round(target), "water_today_ml": data["water"].get(today(), 0),
           "workout_streak": streak(data["workouts"])}
    system = (f"You are FitBuddy, a friendly fitness and nutrition coach. User data: {json.dumps(ctx)}. "
              "Give short, practical, safe advice. Suggest a doctor for medical issues. "
              "Reply in the same language style the user uses (English/Tamil/Tanglish).")
    body = json.dumps({"model": MODEL, "max_tokens": 600, "system": system, "messages": history}).encode()
    req = urllib.request.Request(API_URL, data=body, headers={
        "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)["content"][0]["text"]
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{e.code}: {e.read().decode(errors='ignore')[:300]}")
