import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Game part
if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                print("Password length must be a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    new_password = generate_password(password_length)
    print(f"Your generated password is: {new_password}")