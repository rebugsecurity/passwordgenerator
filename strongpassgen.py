"""
Code by: RebugSecurity | Rebug Security#2166
"""

# Imports:
import random
import string

def generate_password(length=24):
    """
    Function to generate a random password with uppercase letters, lowercase letters, digits
    and special characters!
    """

    # Define value ranges for different character types:
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Use all available characters in the first few positions
    password = []
    password.append(random.choice(lowercase_letters))
    password.append(random.choice(uppercase_letters))
    password.append(random.choice(digits))
    password.append(random.choice(special_chars))

    # Fill in the remaining positions randomly:
    for i in range(length - 4):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    # Now shuffle resulting string and return as a password
    random.shuffle(password)
    return ''.join(password)

# Example usages
password1 = generate_password() # Generates a 24-character password
password2 = generate_password(32) # Generates a 32-character password, obviously for the STRENGTH!