'''Write a program that checks the strength of a password.
A strong password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one number.'''


def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    if has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak: Must include uppercase, lowercase, and a number."

user_pass = input("Enter a password to check: ")
print(check_password_strength(user_pass))