"""
CP1404/CP5632 - Practical
Determine score status - New solution
"""

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
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

if __name__ == "__main__":
    main()
