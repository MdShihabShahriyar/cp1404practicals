class Guitar:
    """Represent a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        current_year = 2022  # Replace with the current year as needed
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 years or older)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Compare two guitars by their year."""
        return self.year < other.year
