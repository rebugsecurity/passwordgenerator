"""
Code by: RebugSecurity | Rebug Security#2166
"""

# Imports:
import string
import secrets

def generate_password(length=24):
    """Generate a random password using secrets module."""

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Example usage:
password = generate_password()  # Generate a password with default length of 12
print("Generated Password:", password)
