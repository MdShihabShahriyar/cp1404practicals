"""
CP1404/CP5632 - Practical - Password Checker
"""

# Constants for password requirements
MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

    password = input("> ")

    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check if length is correct
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for character in password:
        # Count each kind of character
        if character.isdigit():
            number_of_digit += 1
        elif character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # Check if any of the 'normal' counts are zero
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    # Check if special characters are required and return False if none are present
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # If all checks passed, the password is valid
    return True


# Run the main function
if __name__ == "__main__":
    main()
