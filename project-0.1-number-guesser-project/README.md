# 🎯 Number Guesser Game (v0.1)

A beginner-friendly number guessing game written in Python 🐍  
Built in two flavors: a simple single-file version (Solution A) and a modular, scalable version (Solution B).  
The goal? Practice Python — but make it clean, fun, and extendable.

---

## 🧠 Project Goals

- Practice Python basics: input, conditionals, loops, functions  
- Learn modular architecture and clean separation of logic  
- Build a working game: scoring, replay, multiplayer, high score saving  

---

## ✨ Features

- 🎮 2-player turn-based guessing  
- 🔁 Replay without restarting the app  
- 💯 Score system and Game Over handling  
- 💾 High score saving between sessions  
- 🧩 Fully modular structure (Solution B)

---

## 📦 Folder Structure

```
project-0.1-number-guesser-project/
├── Solution-A/                 # Beginner version - all logic in one file
│   └── number_guesser.py
│
├── Solution-B/                 # Modular version (Solution B)
│   ├── src/
│   │   ├── config.py
│   │   ├── number_guesser.py          # Main entry
│   │   ├── data/
│   │   │   └── high_score.txt
│   │   └── game_logic/
│   │       ├── engine.py
│   │       ├── input_handler.py
│   │       ├── score_tracker.py
│   │       ├── game_flow.py
│   │       └── player_manager.py
│   └── requirements.txt
│
└── README.md                  # ← You're here
```

---

## 🚀 How to Run (Solution B)

Make sure you're in the `Solution-B` directory, then run:

\`\`\`bash
python src/number_guesser.py
\`\`\`

---

## ✅ Requirements

- Python 3.10 or newer  
- No external libraries needed (uses standard library: \`random\`, \`os\`, etc.)

---

## 📸 Screenshots *(optional)*

_Add terminal screenshot here if desired later_

---

## 🧪 Tests *(future scope)*

Not included in v0.1, but planned for future versions.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](./LICENSE) file for full details.

---

## 👤 Author

Built with chaos and consistency  
by **Hossein Mehrabi** \`(@meowsawknee)\`  
[GitHub Profile →](https://github.com/meowsawknee)

---

## 📍 Roadmap

- [x] Implement core gameplay  
- [x] Add scoring and replay  
- [x] Create modular version  
- [ ] Add unit tests  
- [ ] Add terminal screenshots  
- [ ] Refactor with argparse
