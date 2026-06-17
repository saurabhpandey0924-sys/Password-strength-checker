import string
import sys
import unicodedata  # Page 7: Unicode Curveball handle karne ke liye

def is_unicode_symbol(char):
    """
    [Page 7] Expand search space from 95 (ASCII) to 143,000+ (Unicode).
    Checks if a character belongs to Punctuation or Symbol categories.
    """
    category = unicodedata.category(char)
    return category.startswith('P') or category.startswith('S')

def check_password_strength():
    # INPUT: Raw Byte Stream / User String Input [Page 8]
    try:
        password = input("Enter a password to check: ")
    except Exception:
        return

    # PROCESS PHASE [Page 8] - Constraint: O(n) Linear Scan Complexity
    
    # [Page 13 - Advanced Feature] Leaked Passwords Set for O(1) optimized lookup
    # Ensures compliance with linear processing constraints
    leaked_passwords = {"password123", "12345678", "qwertyuiop", "admin12345"}
    if password.lower() in leaked_passwords:
        print("\n--- Password Analysis ---")
        print("❌ Security Check: CRITICAL FAILURE")
        print("🔴 Strength: WEAK (Compromised: Common Leaked Password)")
        return

    # 1. Length Verification: The Zero Point [Page 7]
    # < 8 Chars = Immediate Fail (Exponential Brute Force Risk)
    if len(password) < 8:
        print("\n--- Password Analysis ---")
        print("❌ Length ≥ 8 (CRITICAL FAILURE)")
        print("🔴 Strength: WEAK (Immediate Fail: Password too short)")
        return  # Short-Circuit Execution (Fast Fail)

    # 2. Pattern Recognition using Pythonic Elegance [Page 9]
    # Uses C-Optimized built-ins executing a strict O(n) linear scan
    has_upper  = any(char.isupper() for char in password)
    has_digit  = any(char.isdigit() for char in password)
    has_symbol = any(is_unicode_symbol(char) for char in password)

    # Count satisfied logic categories
    score = sum([has_upper, has_digit, has_symbol])

    # OUTPUT: Risk Classification [Page 8]
    print("\n--- Password Analysis ---")
    print(f"Length ≥ 8:       ✅")
    print(f"Uppercase letter: {'✅' if has_upper  else '❌'}")
    print(f"Number:           {'✅' if has_digit  else '❌'}")
    print(f"Symbol (Unicode): {'✅' if has_symbol else '❌'}")
    
    # Strict Tier Classification [Page 4]
    if score == 3:
        print("🟢 Strength: STRONG")
        print("\n--- GATEKEEPER RULE STATUS ---")
        print("🔒 [INPUT VALIDATED. GATEKEEPER PASS.]")
        print("➡️ Ready for Project 2: Forwarding to Argon2id Hashing Pipeline...")
    elif score == 2:
        print("🟡 Strength: MEDIUM")
        print("\n⚠️ Gatekeeper Warning: Entropy is moderate. Encryption blocked until strong.")
    else:
        print("🔴 Strength: WEAK (Missing critical identity safeguards)")
        print("\n❌ Gatekeeper Blocked: Cannot hash what is weak!")

    # Memory Safety: Data in RAM Trap [Page 10]
    # Explicitly wiping the reference to trigger faster memory cleanup
    del password

if __name__ == "__main__":
    check_password_strength()
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)
