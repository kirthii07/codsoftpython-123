import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt user for password length
try:
    length = int(input("Enter desired password length: "))
    if length < 4:
        print("Password length should be at least 4 characters for security.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
