"""
CP1404/CP5632 - Practical
Menu using the standard while loop pattern - New solution
"""

def display_menu():
    """Display the menu."""
    return "(H)ello\n(G)oodbye\n(Q)uit"

def process_choice(choice, name):
    """Process user choice."""
    if choice == "H":
        return f"Hello {name}"
    elif choice == "G":
        return f"Goodbye {name}"
    return "Invalid choice"

def main():
    """Main function to handle the menu."""
    name = input("Enter name: ")
    print(display_menu())
    choice = input(">>> ").upper()
    while choice != "Q":
        result = process_choice(choice, name)
        print(result)
        print(display_menu())
        choice = input(">>> ").upper()
    print("Finished.")

if __name__ == "__main__":
    main()
