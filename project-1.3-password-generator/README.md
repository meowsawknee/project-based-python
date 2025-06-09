# 🔐 Password Generator Project

This project is a fully-featured password generator written in Python, based on an OOP approach.  
Originally inspired by a course project, it has been significantly extended with several practical features.

---

## 🚀 Features

### 🧩 Built-in Generators
- `RandomPasswordGenerator`: Create random passwords with configurable length, digits, symbols, or even custom character sets.
- `MemorablePasswordGenerator`: Generate readable, word-based passwords using the NLTK corpus.
- `PinCodeGenerator`: Numeric PINs with constraints like even-only, odd-only, starts-with digit, and optional checksum.

### ✅ Core Features
- Password strength estimation (Very Weak → Very Strong)
- Export password to `.txt` file
- Copy password to system clipboard (via `pyperclip`)
- Regenerate password easily
- Uniqueness tester (check for duplicate generation across N samples)

### ⚙️ Advanced Options
- Use of `string.ascii_letters`, `string.digits`, `string.punctuation` for clean character control
- Custom character input for advanced random password control
- Allowed digits defined manually (e.g. `allowed_digits = "13579"`)

---

## 🧪 How to Run

```bash
python main.py
```

The `main.py` file includes sample tests for all password generators and features.

---

## 📦 Project Structure

```
project/
│
├── src/
│   ├── base.py
│   ├── pin_generator.py
│   ├── random_generator.py
│   ├── memorable_generator.py
│   └── utils/
│       ├── strength_estimator.py
│       └── uniqueness_tester.py
│
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📚 Dependencies

Generated using `pipreqs`. Key packages used:

- `nltk` (for memorable password generation)
- `pyperclip` (for clipboard functionality)

Install with:

```bash
pip install -r requirements.txt
```

---

## 🌐 Future Plans

- [x] Add CLI and file/clipboard features
- [x] Cover advanced PIN logic
- [ ] Build Streamlit-based UI for end-users
- [ ] Add unit tests to `tests/` folder
- [ ] Option to validate imported passwords

---

## 🧠 Notes

- `string.ascii_letters`, `string.digits`, and `string.punctuation` were used to build character pools.
- The project uses a clean OOP structure with a base class and inheritance.
- Designed to be extensible and testable.

---

## 🔥 Author

Created & maintained by meowsawknee

