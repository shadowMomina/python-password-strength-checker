

# 🔐 Password Strength Checker – Day 25 of 90 Days Python Series

Are you tired of guessing if your password is strong enough? 😅
This beginner-friendly Python tool instantly checks your password’s strength and helps you build safer, smarter passwords. Perfect for anyone learning loops, conditionals, and string handling in Python. 🐍✨

---

## 🧠 Features

✅ Checks password **length** (minimum 8 characters)
✅ Detects **uppercase** and **lowercase** letters
✅ Verifies **numbers** and **special symbols**
✅ Rates password as **Weak**, **Medium**, or **Strong**
✅ Keeps running until you decide to exit

---

## ⚙️ How It Works

Simply run the program, enter your password, and get instant feedback!

### Example:

```
✨ Welcome to the Password Strength Checker ✨

Enter your password: Python@123

✅ Strong Password! Great job 💪
```

The program uses Python’s built-in string methods to evaluate each part of the password and give you a total score based on security strength.

---

## 💡 Concepts Used

* **Loops (`while`)** → keep checking until user exits
* **Conditionals (`if`, `else`)** → evaluate password criteria
* **String methods:**

  * `.isupper()` → check uppercase letters
  * `.islower()` → check lowercase letters
  * `.isdigit()` → check numbers
* **String module** → for punctuation and symbol checking
* **Scoring logic** → to rate password strength

---

## 🧩 Code Overview

Here’s the main logic in short:

```python
import string

while True:
    password = input("Enter your password: ")
    score = 0

    if len(password) >= 8:
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch.islower() for ch in password):
        score += 1
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch in string.punctuation for ch in password):
        score += 1

    if score == 5:
        print("✅ Strong Password! Great job 💪")
    elif 3 <= score < 5:
        print("🟡 Medium Strength Password — could be stronger!")
    else:
        print("🔴 Weak Password — improve your password security!")

    again = input("Do you want to check another password? (yes/no): ").lower()
    if again != "yes":
        break
```

---

## 🚀 How to Run

1. **Download or clone** this repository:

   ```bash
   git clone https://github.com/shadowMomina/python-password-strength-checker.git
   ```
2. **Open terminal or command prompt** in the project folder.
3. Run the script:

   ```bash
   python password_strength_checker.py
   ```

---

## 🌸 About This Project

This project is part of my **90 Days Python Series** — where I build small, fun, and useful projects every day to improve my Python skills.
Day 25 focuses on **practical string handling and logic building** through password validation.

If you’re learning Python, this project is a great way to understand how simple checks can be used to make real-world tools. 💪

---

## 📂 Repository

🔗 [GitHub Repo: python-password-strength-checker](https://github.com/shadowMomina/python-password-strength-checker)

---

## 📜 License

**Self-Independent License (Open for Learning & Use)**

You are free to:

* ✅ Use this code for personal or educational purposes
* ✅ Modify and improve it
* ✅ Share it with credits

**Conditions:**

* Do not sell or distribute this project under your own name without proper attribution.
* Keep the author credit visible: **Created by Momina Raheel (shadowMomina)**.

---

## 💬 Author

👩‍💻 **Momina Raheel**
Building one Python project every day in my *90 Days Python Series!* 🐍
Follow along for more daily coding projects and creative tools! 🌸

