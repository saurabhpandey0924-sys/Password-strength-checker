# 🔐 Password Strength Checker

A Python-based Password Strength Checker that analyzes password security using length validation, uppercase detection, numeric detection, Unicode symbol support, and leaked password detection.

## 🚀 Features

### ✅ Length Verification
- Password must contain at least **8 characters**.
- Short passwords are immediately rejected.

### ✅ Uppercase Detection
Checks whether the password contains at least one uppercase letter.

### ✅ Number Detection
Checks whether the password contains at least one numeric digit.

### ✅ Unicode Symbol Detection
Supports both ASCII and Unicode symbols.

Examples:
- !
- @
- #
- ₹
- €
- ★
- ✓

### ✅ Leaked Password Detection
Blocks commonly used and compromised passwords.

Current blacklist includes:

```python
{
    "password123",
    "12345678",
    "qwertyuiop",
    "admin12345"
}
```

### ✅ Strength Classification

| Score | Strength |
|---------|----------|
| 3/3 | 🟢 Strong |
| 2/3 | 🟡 Medium |
| 0-1/3 | 🔴 Weak |

---

## 📂 Project Structure

```text
Password-Strength-Checker/
│
├── password_checker.py
├── README.md
```

---

## ⚙️ How to Run

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/password-strength-checker.git
```

### Open Folder

```bash
cd password-strength-checker
```

### Run Program

```bash
python password_checker.py
```

---

## 💻 Example Usage

### Strong Password

Input:

```text
MySecurePass123!
```

Output:

```text
Length ≥ 8:       ✅
Uppercase letter: ✅
Number:           ✅
Symbol (Unicode): ✅

🟢 Strength: STRONG
```

### Medium Password

Input:

```text
Password123
```

Output:

```text
Length ≥ 8:       ✅
Uppercase letter: ✅
Number:           ✅
Symbol (Unicode): ❌

🟡 Strength: MEDIUM
```

### Weak Password

Input:

```text
pass
```

Output:

```text
❌ Length ≥ 8 (CRITICAL FAILURE)

🔴 Strength: WEAK
```

---

## 🧠 Algorithm

The program performs:

1. Leaked Password Check
2. Length Validation
3. Uppercase Detection
4. Number Detection
5. Unicode Symbol Detection
6. Password Strength Classification

### Time Complexity

```text
O(n)
```

where n = length of password.

---

## 🔒 Security Notes

- No passwords are stored.
- No passwords are transmitted.
- No user data is saved.
- Passwords are analyzed only during runtime.

---

## 🛠 Built With

- Python 3
- Unicode Character Database
- Cybersecurity Fundamentals

---

## 📈 Future Improvements

- Password Entropy Calculator
- Password Generator
- Argon2id Hashing
- GUI Version
- Web Version
- Password Strength Meter

---

## 👨‍💻 Author

**Saurabh Pandey**

GitHub: https://github.com/Saurabh_Pandey

LinkedIn:linkedin.com/in/saurabh-p-pandey

---

⭐ If you like this project, give it a Star!
