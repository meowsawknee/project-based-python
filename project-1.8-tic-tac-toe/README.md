# 🎮 Tic Tac Toe (Python CLI Version)

A modular, interactive version of the classic Tic Tac Toe game, built entirely in Python using Object-Oriented Programming.  
Play against another player or challenge a basic AI opponent — all within your terminal, with colorful output and a clean interface.

---

## 📂 Project Structure

```
project-1.8-tic-tac-toe/
├── src/
│   ├── ai.py              # Simple AI logic
│   ├── game.py            # Core game mechanics
│   ├── cli.py             # CLI interface and game loop
│   └── __pycache__/
│
├── README.md
├── requirements.txt
├── streamlit_app.py       # Optional: future web version
├── test.py, test.ipynb    # Early tests and notes
```

---

## 🚀 Features

- 🔁 Play against Human or AI
- 🎯 Win detection and scoreboard
- 🎨 Terminal UI with colors (`colorama`)
- 🧠 AI opponent with random move logic (can be upgraded)
- 🔄 Match replay with score tracking
- 🧼 Clean modular code (OOP, Type Hinting, Docstrings)

---

## 📥 Installation

Make sure Python 3.10+ is installed.

```bash
git clone https://github.com/meowsawknee/tic-tac-toe-python.git
cd tic-tac-toe-python
pip install -r requirements.txt
```

---

## ▶️ Run the Game

```bash
python src/cli.py
```

---

## 🧠 What I Learned

This project was built as a hands-on learning experience.  
Key concepts and tools I practiced:

- ✅ Object-Oriented Programming in Python
- ✅ Using `self`, instance attributes, and methods
- ✅ Modular architecture & separation of concerns
- ✅ Simple AI logic with `random.choice`
- ✅ Type hinting & writing docstrings
- ✅ Exception handling with `try`/`except`
- ✅ CLI enhancements with `colorama`
- ✅ Score tracking using dictionaries
- ✅ Git-based version control
- ✅ Building `requirements.txt` via `pipreqs`

---

## 📌 Future Ideas

- [ ] Difficulty levels for AI (Minimax or rule-based)
- [ ] Save match history to file (JSON or CSV)
- [ ] Sound effects or terminal animations
- [ ] Web version with Streamlit *(planned)*
- [ ] Pixel-art visuals and custom icons via Streamlit
- [ ] Theme switcher: classic / cyberpunk / retro

---

## 💡 Credits

Originally inspired by a course assignment (Pytopia),  
but extended step-by-step with clean structure, design, and new features.

---

## 🛠 Built With

- Python 3.10+
- [`colorama`](https://pypi.org/project/colorama/) — for colorful terminal UI
