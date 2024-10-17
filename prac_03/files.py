"""
CP1404/CP5632 Practical - Suggested Solution
Make the appropriate choice of file-reading technique for each of these questions:
- read()
- readline()
- readlines()
- for line in file
"""

# 1.
# We can write using print or write; in most cases, print is easier and more familiar
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)  # Write the name to the file
out_file.close()  # Close the file

# 2.
# Here we choose read() because we want the whole contents
in_file = open("name.txt", "r")
name = in_file.read().strip()  # Read the entire content and remove whitespace
in_file.close()  # Close the file
print(f"Hi {name}!")  # Greet the user

# 3.
# Here we choose readline() because we need separate lines, and we don't want every line
# It would be inefficient to use readlines() and then select only the first 2 values
with open("numbers.txt", "r") as in_file:  # Use with for safe file handling
    number1 = int(in_file.readline().strip())  # Read the first number
    number2 = int(in_file.readline().strip())  # Read the second number
print(number1 + number2)  # Print the sum of the first two numbers

# 4.
# Here we choose for line in file because we want every line
total = 0  # Initialize total
with open("numbers.txt", "r") as in_file:  # Use with for safe file handling
    for line in in_file:  # Iterate through each line
        total += int(line.strip())  # Convert to int and add to total
print(total)  # Print the total of all numbers
