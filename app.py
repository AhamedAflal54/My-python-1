import string
import random

def generate_password(length=8, use_special_chars=False):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")

    # Get user input
    length = int(input("Enter the desired length of the password: "))
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate password
    password = generate_password(length, use_special_chars)

    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
