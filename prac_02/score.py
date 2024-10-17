"""
CP1404/CP5632 - Practical
Determine score status
"""

import random  # Importing random to generate random scores

def evaluate_score(score):
    """Determine the status based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    return "Bad"

def main():
    """Main function to get user input and evaluate score."""
    # Get user score
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

    # Generate a random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}, Result: {evaluate_score(random_score)}")

if __name__ == "__main__":
    main()



