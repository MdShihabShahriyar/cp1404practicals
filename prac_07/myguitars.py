import csv
from guitar import Guitar  # Assuming Guitar class is in guitar.py


def read_guitars_from_file(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(f"Reading row: {row}")  # Debug print
                    name, year, cost = row
                    guitars.append(Guitar(name, int(year), float(cost)))
        print(f"Total guitars read: {len(guitars)}")  # Debug print
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    if not guitars:
        print("No guitars to display.")
    for guitar in guitars:
        print(guitar)


def sort_guitars(guitars):
    """Sort the guitars by year."""
    guitars.sort()  # Will use the __lt__ method in Guitar to compare by year


def main():
    # Step 1: Read guitars from CSV
    filename = 'guitars.csv'  # Make sure guitars.csv is in the same folder
    guitars = read_guitars_from_file(filename)

    if guitars:
        print("\nGuitars read from file:")
        display_guitars(guitars)

        # Step 2: Sort guitars by year and display sorted list
        sort_guitars(guitars)
        print("\nGuitars sorted by year:")
        display_guitars(guitars)


if __name__ == "__main__":
    main()
