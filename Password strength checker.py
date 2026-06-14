import string

def check_password_strength(password):
    # 1. Length Verification: The Zero Point (Immediate Fail Rule)
    # Less than 8 characters means immediate fail due to brute force risk
    if len(password) < 8:
        print("\n--- Password Analysis ---")
        print("❌ Length ≥ 8 (CRITICAL FAILURE)")
        print("🔴 Strength: WEAK (Immediate Fail: Password too short)")
        return  # Baki ke validation checks chalenge hi nahi (Fast Fail)

    # 2. Pattern Recognition (Only runs if password length is >= 8)
    has_upper  = any(char.isupper() for char in password)
    has_digit  = any(char.isdigit() for char in password)
    
    # Expanding search space to all standard symbols
    has_symbol = any(char in string.punctuation for char in password)

    # Count how many of the 3 remaining pattern conditions are met
    score = sum([has_upper, has_digit, has_symbol])

    # 3. Display Feedback & Output Risk Classification
    print("\n--- Password Analysis ---")
    print(f"Length ≥ 8:       ✅")
    print(f"Uppercase letter: {'✅' if has_upper  else '❌'}")
    print(f"Number:           {'✅' if has_digit  else '❌'}")
    print(f"Symbol:           {'✅' if has_symbol else '❌'}")
    
    # Strict Tier Classification based on satisfied categories
    if score == 3:
        print("🟢 Strength: STRONG")
    elif score == 2:
        print("🟡 Strength: MEDIUM")
    else:
        print("🔴 Strength: WEAK (Missing character variety)")

# Run the program
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)