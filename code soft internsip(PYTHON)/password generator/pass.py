import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for security.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")

# Get user input for password length
length = int(input("Enter desired password length: "))
generate_password(length)