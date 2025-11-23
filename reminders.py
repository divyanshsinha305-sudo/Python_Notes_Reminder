from datetime import datetime
from storage import get_reminders, get_note_by_id, mark_reminder_notified

def check_due_reminders():
    reminders = get_reminders()
    now = datetime.utcnow()

    due_list = []

    for r in reminders:
        reminder_time = datetime.fromisoformat(r["time"])
        if reminder_time <= now and not r["notified"]:
            note = get_note_by_id(r["note_id"])
            due_list.append((note, r))
            mark_reminder_notified(r["note_id"], r["time"])

    return due_list
