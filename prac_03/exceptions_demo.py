"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError will occur if the user inputs a value that cannot be converted to an integer (e.g., if they enter a string like 'abc').

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError will occur if the user enters zero for the denominator, as division by zero is not defined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, we can add a check to ensure the denominator is not zero before performing the division.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check for zero denominator to avoid ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero!")  # Print error message
    else:
        fraction = numerator / denominator
        print(f"The result is: {fraction}")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
