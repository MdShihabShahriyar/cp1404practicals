"""
CP1404/CP5632 - Practical
Loops - New solution
"""

def print_odd_numbers():
    """Print odd numbers from 1 to 20."""
    for i in range(1, 21, 2):
        print(i, end=" ")
    print()

def count_in_tens():
    """Count in 10s from 0 to 100."""
    for i in range(0, 101, 10):
        print(i, end=" ")
    print()

def count_down():
    """Count down from 20 to 1."""
    for i in range(20, 0, -1):
        print(i, end=" ")
    print()

def print_stars(n):
    """Print n stars on one line."""
    for _ in range(n):
        print('*', end=' ')
    print()

def print_increasing_stars(n):
    """Print n lines of increasing stars."""
    for i in range(1, n + 1):
        print('*' * i)

def main():
    """Main function for loop exercises."""
    print_odd_numbers()
    count_in_tens()
    count_down()

    number_of_stars = int(input("Number of stars: "))
    print_stars(number_of_stars)
    print_increasing_stars(number_of_stars)

if __name__ == "__main__":
    main()
