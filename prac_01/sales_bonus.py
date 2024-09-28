"""
CP1404/CP5632 - Practical
Sales bonus program - New solution
"""

def calculate_bonus(sales):
    """Calculate the bonus based on sales."""
    if sales < 1000:
        return sales * 0.1
    return sales * 0.15

def main():
    """Sales bonus calculator with loop."""
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print(f"Bonus is ${bonus:.2f}")
        sales = float(input("Enter sales: $"))

if __name__ == "__main__":
    main()
