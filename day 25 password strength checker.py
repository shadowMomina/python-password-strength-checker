# 🔐 Password Strength Checker
# Day 25 of 90 Days Python Series by Momina Raheel

# Importing 'string' to easily access letters, digits, and punctuation
import string

print("✨ Welcome to the Password Strength Checker ✨")

while True:
    password = input("\nEnter your password: ")

    # Initialize score
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password is too short. (Use at least 8 characters)")

    # Check for uppercase letters
    if any(ch.isupper() for ch in password):
        score += 1
    else:
        print("⚠️ Add at least one uppercase letter.")

    # Check for lowercase letters
    if any(ch.islower() for ch in password):
        score += 1
    else:
        print("⚠️ Add at least one lowercase letter.")

    # Check for digits
    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        print("⚠️ Add at least one number.")

    # Check for special symbols
    if any(ch in string.punctuation for ch in password):
        score += 1
    else:
        print("⚠️ Add at least one special character (e.g. !, @, #, $).")

    # Final strength evaluation
    if score == 5:
        print("✅ Strong Password! Great job 💪")
    elif 3 <= score < 5:
        print("🟡 Medium Strength Password — could be stronger!")
    else:
        print("🔴 Weak Password — improve your password security!")

    # Option to check again
    again = input("\nDo you want to check another password? (yes/no): ").lower()
    if again != "yes":
        print("\nThanks for using the Password Strength Checker! 🔒")
        break
