"""
Emails to Names Dictionary
Estimate: 25 minutes
Actual: 22 minutes
"""


def main():
    """Store emails and names in a dictionary, asking user for confirmation."""
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        # Extract name from the email
        name = get_name_from_email(email)
        # Ask if the extracted name is correct
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        # If the user says no or presses anything besides Y, ask for the correct name
        if confirmation != "y" and confirmation != "":
            name = input("Name: ").title()

        # Store the email and name in the dictionary
        email_to_name[email] = name

        # Ask for the next email
        email = input("Email: ")

    # After all emails are entered, print the results
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract the name from an email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    # Join parts of the name and convert it to title case
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()
