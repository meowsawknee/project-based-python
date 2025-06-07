# 🪨 Rock Paper Scissors Game (Project 1.1)

This project is a Python-based implementation of the classic game "Rock, Paper, Scissors", created as part of the Pytopia beginner-to-intermediate course. The game runs in the terminal and features a user vs. computer match with random choices, input validation, and a simple scoring system.

> 💬 *"I didn’t follow the suggested flat structure — I built a modular version first to clear my head and understand what’s really needed. I plan to build the flat version too, purely for practice."*

---

## 📁 Project Structure

\`\`\`
project-1.1-rock-paper-scissors/
│
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── engine.py      # Core game logic and score tracking
│   │   ├── player.py      # Handles user input with validation
│   │   └── computer.py    # Generates random choices for the computer
│   └── main.py            # Entry point that runs the game loop
│
├── tests/
│   └── test_engine.py     # Unit tests for determine_winner()
│
├── README.md
├── requirements.txt
└── .vscode/launch.json    # Optional: for VSCode debugging
\`\`\`

---

## 🎮 How to Play

Run the game from the root directory:

\`\`\`bash
python src/main.py
\`\`\`

- Type \`rock\`, \`paper\`, or \`scissors\` to play  
- Type \`q\` to quit the game  
- First player to reach 5 points wins!

---

## 🚀 Features

- Full game loop with replay logic  
- Score system (first to 5 wins)  
- User input validation  
- Randomized computer moves  
- Modular code with separation of concerns  
- Unit tests using \`unittest\`

---

## 🧪 Running Tests

To run the tests:

\`\`\`bash
PYTHONPATH=src python -m unittest tests.test_engine
\`\`\`

---

## 📚 Learning Outcomes

This project helped me understand:

- How to apply Object-Oriented Programming (OOP) in Python  
- How to build modular programs with multiple files and imports  
- How to write basic unit tests and structure them properly  
- How to debug tricky import issues and structure execution cleanly

---

## ✍️ Personal Notes

This was my first time working with unit tests. It was a weird but satisfying experience and I’m planning to get more fluent with it over time.

I had a few issues with Python imports at first, but I’ll be reviewing that lesson again to strengthen my foundation.

Overall, it was a super valuable and practical project.

---

## ✅ Requirements

- Python 3.7+
- No external packages required (uses only Python standard library)
