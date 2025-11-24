Personal Notes & Reminder System

*A Python-based CLI tool for managing notes and scheduling reminders.*

---
Introduction

The **Personal Notes & Reminder System** is a Python-based application designed to help users organize their notes, store ideas, and manage reminders effectively. In today's fast-moving environment, individuals often rely on scattered files, handwritten notes, or multiple mobile applications, making it difficult to track important information.

This project provides a **simple, offline, and reliable command-line interface (CLI)** that allows users to:

* Create and manage notes
* Search notes instantly
* Store data locally using JSON
* Set reminders with timestamps
* Export notes as CSV

It demonstrates core programming concepts suitable for beginner Python developers, such as modular design, file handling, timestamps, and user-driven interfaces.

---
Problem Statement

Users often struggle with disorganized storage of notes and frequent forgetting of tasks due to:

* Scattered handwritten notes
* Dependence on heavy mobile applications
* Lack of a simple offline tool
* Difficulty managing tasks and deadlines

Thus, there is a requirement for a **lightweight, offline note-taking and reminder management system** that is:

* Easy
* Reliable
* Beginner-friendly
* Completely local (no internet required)

---
Functional Requirements

1. **Create Notes**
2. **View Notes**
3. **Edit Notes**
4. **Delete Notes**
5. **Search Notes (title/body/tags)**
6. **Set Reminders**
7. **Check Due Reminders**
8. **Export Notes to CSV**
9. **Store Data Persistently Using JSON**

---
Non-Functional Requirements

Usability

* Simple CLI (command-line interface)
* Easy navigation and clear user prompts

Reliability

* JSON ensures consistent storage
* Accurate timestamps using `datetime`

Scalability

* More features/modules can be added easily

Maintainability

* Clean modular codebase
* Separate modules for each feature

---
System Architecture

1.Presentation Layer (CLI UI)**

Handles user interaction through command-line menu.

2.Application Logic

Processes actions:

* Create/edit/delete notes
* Search notes
* Handle reminders

3.Data Storage Layer

* Stores notes in JSON
* Exports notes using CSV

---

Module Breakdown

4.storage.py

* Handles JSON read/write
* CRUD operations
* Reminder storage

notes_app.py

* Main CLI menu
* User input handling

utils.py

* Search system
* CSV exporting

reminders.py

* Processes due reminders

---

##  Text Diagram Representations

###  Use Case Diagram (Text Form)

* User → Create Note
* User → Edit Note
* User → Delete Note
* User → Search Notes
* User → Set Reminder
* User → Export Notes

###  Workflow (Creating a Note)

1. Start
2. Display menu
3. Choose "Create Note"
4. Enter details
5. Save in JSON
6. Display success

###  Sequence Diagram

1. User selects an option
2. UI sends data to logic layer
3. Logic updates storage
4. Storage returns success
5. UI displays result

---

## Design Decisions

### Why Python?

* Clean syntax
* Easy to learn
* Powerful file-handling libraries

### Why CLI?

* No GUI complexity
* Lightweight and fast
* Perfect for first-year projects

### Why JSON?

* Easy to read
* Lightweight
* Perfect for simple data storage

### Timestamp Reminders

* Ensures accuracy
* Prevents manual entry errors

---

## Implementation Details

### Python Modules Used

* `json`
* `datetime`
* `csv`
* `os`

### Project Structure

```
project/
├── notes_app.py
├── storage.py
├── utils.py
├── reminders.py
└── notes.json
```

---

## Core Features

* CRUD for notes
* Keyword search
* Reminder scheduling
* CSV export
* Persistent JSON storage

---

## Testing Overview

Unit Tests

* Notes CRUD
* Reminder logic
* Search feature

Integration Tests

Create → Edit → Export

Functional Tests
* All menu options checked
  
Boundary Tests
* Empty notes
* Invalid timestamps
* Missing JSON file

---

Challenges Faced

* Maintaining clean JSON structure
* Handling invalid user input
* Preventing duplicate reminders
* Designing a modular structure

---

Learnings & Takeaways

* Better understanding of Python basics
* Real-world file handling
* Modular system design
* Strong documentation practice
* Debugging and validation techniques

---

Future Enhancements

* GUI using Tkinter
* Cloud-sync notes
* Mobile app version
* Multiple reminder types
* Color-coded notes
* Login/user authentication

---

References

* Python Documentation
* W3Schools
* GeeksforGeeks
* StackOverflow
* Class lectures and notes

---
## 🙏 THANK YOU!
