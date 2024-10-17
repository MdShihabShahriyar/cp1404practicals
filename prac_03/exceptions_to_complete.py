"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False  # Start with is_finished set to False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))  # Prompt for integer input
        is_finished = True  # Exit the loop if input is valid
    except ValueError:  # Handle the case where input is not a valid integer
        print("Please enter a valid integer.")  # Inform the user of the error

print("Valid result is:", result)  # Display the valid integer entered
