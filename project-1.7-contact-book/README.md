# 📒 Contact Book (Python CLI + JSON Storage)

This is a simple and extensible **Contact Book** project written in Python.  
It provides a Command-Line Interface (CLI) to manage contacts with support for **Create, Read, Update, Delete (CRUD)** operations.  
All contact data is saved to a local JSON file (), so nothing is lost when the program closes.

---

## ✨ Features

- Add, edit, delete, and view contacts via CLI
- Persistent data storage using JSON
- Clean modular architecture (`src/` folder)
- Pretty printed output using `PrettyTable`
- Type hints and docstrings for readability and maintainability

---

## 📁 Project Structure

```
.
├── main.py
├── requirements.txt
├── README.md
├── contacts.json
├── test.ipynb
├── test.py
└── src/
    ├── __init__.py
    ├── cli.py
    └── contact_book.py
```

---

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

---

## 📌 Notes

This version is fully functional and production-ready.  
There are ideas to extend this further in the future — for example, adding a GUI, exporting to CSV, or syncing with a database.

Stay tuned.

---

## 📄 License

MIT License
