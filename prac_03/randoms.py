# randoms.py

# Import the random module to access its functions
import random

# Line 1: Generates a random integer between 5 and 20 inclusive
print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# You will see a random integer between 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5, and the largest number is 20.

# Line 2: Generates a random number from the range 3 to 10 with a step of 2
print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# You will see a random number from the set {3, 5, 7, 9}.
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3, and the largest number is 9.
# Could line 2 have produced a 4?
# No, line 2 could not produce a 4, as it only produces odd numbers in this range.

# Line 3: Generates a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# You will see a random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.5, and the largest number is 5.5.

# Produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100 inclusive: {random_number}")
