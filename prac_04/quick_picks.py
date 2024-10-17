"""
CP1404/CP5632 Practical
Quick pick program
"""

import random

# Defining constants for the program
NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Generate a set of quick pick lottery numbers."""
    # Ask the user how many quick picks they want
    number_of_quick_picks = int(input("How many quick picks? "))

    # Validate input
    while number_of_quick_picks < 0:
        print("Invalid input! Number of quick picks must be positive.")
        number_of_quick_picks = int(input("How many quick picks? "))

    # Generate each quick pick
    for i in range(number_of_quick_picks):
        quick_pick = []

        # Ensure no repeated numbers
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MINIMUM, MAXIMUM)
            if number not in quick_pick:
                quick_pick.append(number)

        # Sort and display the quick pick
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


# Run the program
main()
