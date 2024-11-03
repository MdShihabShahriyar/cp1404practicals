from guitar import Guitar


def main():
    """Main function to manage guitar collection."""
    print("My guitars!")

    guitars = []

    # User input section
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost_input = input("Cost: $")

        # Remove the dollar sign and convert to float
        cost = float(cost_input.replace('$', '').replace(',', '').strip())

        # Create a new Guitar instance and add it to the list
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")

    # Print the details of all guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
