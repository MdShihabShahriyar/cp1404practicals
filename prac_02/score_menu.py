""" Score Menu Application """

# Import necessary libraries
import random  # Used for generating random scores

# Define constants for score limits
LOW_SCORE = 0
HIGH_SCORE = 100

def main():
    """ Entry point of the program, contains the menu logic """
    print("Welcome to the Score Menu Application!")

    # Get the initial score from the user
    user_score = get_score()

    while True:
        # Display the menu options
        display_menu()
        user_choice = input("Select an option: ").strip().upper()

        if user_choice == 'G':
            user_score = get_score()
        elif user_choice == 'P':
            display_result(user_score)
        elif user_choice == 'S':
            print_stars(user_score)
        elif user_choice == 'Q':
            print("Thank you for using the Score Menu Application! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def display_menu():
    """ Display the main menu """
    print("\nMenu Options:")
    print("(G) Get a valid score")
    print("(P) Print result")
    print("(S) Show stars")
    print("(Q) Quit")

def get_score():
    """ Prompt the user for a valid score within the defined range """
    while True:
        try:
            score = int(input(f"Please enter a score between {LOW_SCORE} and {HIGH_SCORE}: "))
            if LOW_SCORE <= score <= HIGH_SCORE:
                return score
            else:
                print(f"Score must be in the range {LOW_SCORE} to {HIGH_SCORE}.")
        except ValueError:
            print("Oops! That was not a valid number. Try again.")

def display_result(score):
    """ Print the score result using a function from score.py """
    from score import determine_result  # Import the function for score evaluation
    result = determine_result(score)
    print(f"Your result is: {result}")

def print_stars(score):
    """ Print a line of stars based on the user's score """
    print("*" * score)

# Standard way to start the program
if __name__ == "__main__":
    main()
