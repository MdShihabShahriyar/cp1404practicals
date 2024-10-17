"""
CP1404/CP5632 Practical
Lists "warm-up"
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# My predictions:
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False (because '3' is a string, not an integer)
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Running the code in Python console will confirm the predictions.

# Now, modify the list as per the instructions:

# Change the first element of numbers to "ten" (the string)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
