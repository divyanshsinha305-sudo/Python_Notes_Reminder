from storage import (
    init_storage, add_note, list_notes, get_note_by_id,
    update_note, delete_note, add_reminder
)
from utils import search_notes, export_notes_csv
from reminders import check_due_reminders

def show_menu():
    print("\n==== Personal Notes & Reminder System ====")
    print("1. Create Note")
    print("2. List Notes")
    print("3. View Note")
    print("4. Edit Note")
    print("5. Delete Note")
    print("6. Search Notes")
    print("7. Export Notes (CSV)")
    print("8. Set Reminder for Note")
    print("9. Check Reminders")
    print("0. Exit")
    print("==========================================")

def create_note():
    title = input("Enter title: ")
    body = input("Enter body: ")
    tags = input("Enter tags (comma separated): ").split(",")
    note = add_note(title, body, tags)
    print("Note created:", note)

def list_all_notes():
    notes = list_notes()
    for n in notes:
        print(f"{n['id']}. {n['title']}  (tags: {', '.join(n['tags'])})")

def view_note():
    note_id = int(input("Enter note ID: "))
    n = get_note_by_id(note_id)
    if n:
        print("\n--- Note Details ---")
        print("Title:", n["title"])
        print("Body:", n["body"])
        print("Tags:", ", ".join(n["tags"]))
        print("Created:", n["created_at"])
        print("Updated:", n["updated_at"])
    else:
        print("Note not found.")

def edit_note():
    note_id = int(input("Enter note ID: "))
    n = get_note_by_id(note_id)
    if not n:
        print("Note not found.")
        return
    title = input("New title (leave blank to keep same): ")
    body = input("New body (leave blank to keep same): ")
    tags = input("New tags (comma separated, leave blank to keep same): ")

    update_note(
        note_id,
        title if title else None,
        body if body else None,
        tags.split(",") if tags else None
    )
    print("Note updated.")

def delete_note_cli():
    note_id = int(input("Enter note ID: "))
    delete_note(note_id)
    print("Note deleted.")

def search_cli():
    keyword = input("Enter keyword: ")
    results = search_notes(list_notes(), keyword)
    print(f"\nFound {len(results)} results:")
    for r in results:
        print(f"{r['id']}. {r['title']}")

def set_reminder_cli():
    note_id = int(input("Enter note ID: "))
    time_str = input("Enter reminder time (YYYY-MM-DD HH:MM): ")
    # convert to ISO format
    iso_time = time_str.replace(" ", "T") + ":00"
    add_reminder(note_id, iso_time)
    print("Reminder added!")

def check_reminders_cli():
    due = check_due_reminders()
    if due:
        print("\n=== REMINDERS DUE ===")
        for note, r in due:
            print(f"Reminder for Note {note['id']} - {note['title']}")
            print(f"Scheduled at: {r['time']}")
    else:
        print("No reminders due.")

def main():
    init_storage()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1": create_note()
        elif choice == "2": list_all_notes()
        elif choice == "3": view_note()
        elif choice == "4": edit_note()
        elif choice == "5": delete_note_cli()
        elif choice == "6": search_cli()
        elif choice == "7":
            export_notes_csv(list_notes())
            print("Notes exported to notes_export.csv")
        elif choice == "8": set_reminder_cli()
        elif choice == "9": check_reminders_cli()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
