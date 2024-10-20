"""
Wimbledon Data Processing
Estimate: 35 minutes
Actual: 40 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    """Read the data file, process, and display Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_count, countries = process_records(records)
    display_results(champion_count, countries)

def get_records(filename):
    """Read the file and return a list of records (list of lists)."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # Skip the header row
        for line in file:
            parts = line.strip().split(",")  # Split the line into parts
            records.append(parts)  # Add the parts as a list to records
    return records

def process_records(records):
    """Process records to create a champion count dictionary and a set of countries."""
    champion_count = {}
    countries = set()

    for record in records:
        # Add country to the set
        countries.add(record[INDEX_COUNTRY])

        # Count champion wins
        champion = record[INDEX_CHAMPION]
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1

    return champion_count, countries

def display_results(champion_count, countries):
    """Display the processed results: champions and their win count, and countries."""
    print("Wimbledon Champions:")
    for champion, count in champion_count.items():
        print(f"{champion} {count}")

    # Sort the countries alphabetically and display
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()
