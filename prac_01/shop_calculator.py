"""
CP1404/CP5632 - Practical
Shop calculator program - New solution
"""

def calculate_total_price(number_of_items, prices):
    """Calculate total price with potential discount."""
    total = sum(prices)
    if total > 100:
        total *= 0.9
    return total

def main():
    """Shop calculator with item price and discount logic."""
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    prices = []
    for _ in range(number_of_items):
        price = float(input("Price of item: "))
        prices.append(price)

    total = calculate_total_price(number_of_items, prices)
    print(f"Total price for {number_of_items} items is ${total:.2f}")

if __name__ == "__main__":
    main()
