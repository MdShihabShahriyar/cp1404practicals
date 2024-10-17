import random

# Constants
MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
FILENAME = "stock_price_simulation.txt"  # Output file

# Open output file for writing
out_file = open(FILENAME, 'w')

price = INITIAL_PRICE
day = 0
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1  # Increment day counter
    # Generate a random integer of 1 or 2 for increase or decrease
    if random.randint(1, 2) == 1:  # 50% chance for increase
        # Generate a random floating-point number between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:  # 50% chance for decrease
        # Generate a random floating-point number between -MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)  # Update price based on change
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

# Close the output file when finished
out_file.close()
