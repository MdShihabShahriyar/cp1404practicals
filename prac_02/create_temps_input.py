import random

def create_temps_input(filename):
    """Create a text file with random float temperatures."""
    with open(filename, 'w') as file:
        for _ in range(15):  # Generate 15 random temperatures
            temperature = random.uniform(-200, 200)  # Random float between -200 and +200
            file.write(f"{temperature}\n")

if __name__ == "__main__":
    create_temps_input('temps_input.txt')
    print("temps_input.txt has been created with random temperatures.")
