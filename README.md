# Student Registration System 🎓

A CLI-based Student Registration System built in Python using Object-Oriented
Programming and JSON file persistence — no external database or framework
dependencies.

---

## 📖 Overview

This is a menu-driven command-line application for managing student records
(add, view, search, update, delete). It's a deliberately small, self-contained
project used to practice core Python fundamentals — classes, exception
handling, and file-based persistence — before moving on to database-backed
and framework-based projects like [MailBrain](https://github.com/MukeshK25-dev/MailBrain).

---

## 🚀 Features
- Add new students (with duplicate ID check)
- View all students
- Search student by ID
- Update student details (with duplicate ID check on the new ID)
- Delete student records
- Persistent storage using a local JSON file (`stud.json`)
- Input validation via exception handling on every numeric field

---

## 🛠️ Tech Stack
- Python 3 (standard library only)
- JSON for data storage
- Object-Oriented Programming (no external dependencies)

---

## ⚙️ Installation & Usage

```bash
# Clone the repository
git clone https://github.com/MukeshK25-dev/Student-Registration-System.git
cd Student-Registration-System

# Run the program (no dependencies to install)
python3 student_management.py
```

You'll be dropped into a numbered menu (Add / View / Search / Update / Delete / Exit).
Data is saved to `stud.json` in the same folder after every add/update/delete.

---

## 📂 Project Structure

```text
Student-Registration-System/
├── student_management.py   # Entire application: Student class + CLI menu loop
├── stud.json                # Generated at runtime — student records (not committed)
├── LICENSE
├── .gitignore
└── README.md
```

This is currently a **single-file application** by design — it's scoped as a
fundamentals exercise, not a production system. See [Future Improvements](#-future-improvements)
for how this would be restructured for a larger project.

---

## 📌 Concepts Used
- OOP (classes, objects, `__init__`, instance methods)
- Exception handling (`try` / `except` on all numeric input)
- File handling (JSON read/write)
- Lists and dictionaries as in-memory + serialized data structures
- Menu-driven CLI control flow

---

## 🔮 Future Improvements
- Split into a proper module layout (`models/`, `services/`, `cli.py`) instead of one file
- Replace JSON storage with SQLite/MySQL for real persistence guarantees
- Add automated tests with `pytest`
- Web UI using Flask/FastAPI

---

## 📝 License
MIT — see [LICENSE](./LICENSE).

## 👨‍💻 Author
**Mukesh K** — B.Tech Information Technology
