import random
import string
import os

# Define ANSI escape codes for colors
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'

def clear_console():
    """Clears the console."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True):
    # """Generates a random password with the specified settings."""
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to get integer input from user
def get_integer_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Please enter a valid integer!")

# Settings menu with colored text
def settings_menu():
    print(GREEN + "Password settings:" + RESET)
    print("1. " + YELLOW + "Modify password length" + RESET + " (current:", password_length, ")")
    print("2. " + YELLOW + "Toggle lowercase letters" + RESET + " (current:", use_lowercase, ")")
    print("3. " + YELLOW + "Toggle uppercase letters" + RESET + " (current:", use_uppercase, ")")
    print("4. " + YELLOW + "Toggle digits" + RESET + " (current:", use_digits, ")")
    print("5. " + YELLOW + "Toggle punctuation characters" + RESET + " (current:", use_punctuation, ")")
    print("6. " + YELLOW + "Generate password" + RESET)
    print("7. " + RED + "Exit" + RESET)

# Initial settings
password_length = 12
use_lowercase = True
use_uppercase = True
use_digits = True
use_punctuation = True

while True:
    clear_console()
    settings_menu()
    choice = get_integer_input("Choose an option: ")

    if choice == 1:
        password_length = get_integer_input("Enter the new password length: ")
    elif choice == 2:
        use_lowercase = not use_lowercase
    elif choice == 3:
        use_uppercase = not use_uppercase
    elif choice == 4:
        use_digits = not use_digits
    elif choice == 5:
        use_punctuation = not use_punctuation
    elif choice == 6:
        password = generate_password(
            length=password_length,
            use_lowercase=use_lowercase,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_punctuation=use_punctuation
        )
        print("Your generated password is:", YELLOW + password + RESET)
        input("Press Enter to continue...")
    elif choice == 7:
        print(RED + "Thank you for using the password generator!" + RESET)
        break
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")
