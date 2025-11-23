import json
import os
from datetime import datetime

FILE_PATH = "notes.json"

def init_storage():
    """Initialize JSON file if not present."""
    if not os.path.exists(FILE_PATH):
        data = {"notes": [], "reminders": []}
        save_data(data)

def load_data():
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def add_note(title, body, tags):
    data = load_data()
    new_id = 1 if len(data["notes"]) == 0 else data["notes"][-1]["id"] + 1

    note = {
        "id": new_id,
        "title": title,
        "body": body,
        "tags": tags,
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": None
    }

    data["notes"].append(note)
    save_data(data)
    return note

def list_notes():
    data = load_data()
    return data["notes"]

def get_note_by_id(note_id):
    data = load_data()
    for note in data["notes"]:
        if note["id"] == note_id:
            return note
    return None

def update_note(note_id, title=None, body=None, tags=None):
    data = load_data()
    for note in data["notes"]:
        if note["id"] == note_id:
            if title: note["title"] = title
            if body: note["body"] = body
            if tags: note["tags"] = tags
            note["updated_at"] = datetime.utcnow().isoformat()
            save_data(data)
            return note
    return None

def delete_note(note_id):
    data = load_data()
    data["notes"] = [n for n in data["notes"] if n["id"] != note_id]
    save_data(data)

def add_reminder(note_id, time_str):
    data = load_data()
    reminder = {
        "note_id": note_id,
        "time": time_str,
        "notified": False
    }
    data["reminders"].append(reminder)
    save_data(data)

def get_reminders():
    data = load_data()
    return data["reminders"]

def mark_reminder_notified(note_id, time_str):
    data = load_data()
    for r in data["reminders"]:
        if r["note_id"] == note_id and r["time"] == time_str:
            r["notified"] = True
    save_data(data)
