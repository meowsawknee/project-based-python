# 🎉 Happy Number Checker

This is a simple Python program that determines whether a number is a **happy number** or not.

A number is considered *happy* if the process of repeatedly summing the squares of its digits eventually leads to `1`. If it enters a cycle that doesn’t include `1`, it is called *unhappy*.

---

## 🧮 Example

**Input:** 19  
**Steps:**
1² + 9² = 82  
8² + 2² = 68  
6² + 8² = 100  
1² + 0² + 0² = 1 ✅

**Output:** Happy Number 🎉

---

## 📁 Project Structure
```
.
├── run.py                     # Main script to take user input and check happiness
├── test_happy_number.py       # Simple test file with assert statements
├── README.md                  # You're reading it :)
├── happy-numbers_test_1.ipynb # Jupyter test notebook
├── .gitignore                 # Ignore Python cache and temp files

```
---

## ▶️ How to Run

💻 Run the program:

    python run.py

✅ Run tests:

    python test_happy_number.py

You should see:

    ✅ All tests passed!

---

## 💡 Notes

- Input validation is included (only accepts positive integers).
- Tests are written using native `assert` statements.
- Fully terminal-based, beginner-friendly!

---

## 📦 Requirements

- Python 3.7+
- No external packages needed — pure Python 🔥

---

## 🧠 Learning Outcomes

- Using loops, sets, and digit processing in Python
- Writing clean functions with return types
- Using assert for basic testing
- Building terminal-based apps with input validation