import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()