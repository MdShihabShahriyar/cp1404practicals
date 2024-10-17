# Set the minimum length for the password
MIN_LENGTH = 6

def main():
    password = input_password()
    print_stars(password)
    print("Password accepted.")

def input_password():
    # Ask the user for a password
    password = get_password()

    return password


def get_password():
    password = input("Enter a password: ")
    # Continue prompting until the password meets the minimum length
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


def print_stars(password):
    # Print stars equal to the length of the password
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


# Call the main function to run the program
main()

