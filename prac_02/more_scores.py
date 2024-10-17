""" Generate Multiple Scores and Evaluate """

import random  # Importing random to generate random scores
from score import evaluate_score  # Import the function from score.py

def main():
    """Main function to handle score generation and file writing."""
    # Ask the user for the number of scores to generate
    num_scores = int(input("How many scores would you like to generate? "))

    # Open a file to write the results
    with open("results.txt", "w") as file:
        for _ in range(num_scores):
            # Generate a random score between 0 and 100
            score = random.randint(0, 100)
            # Evaluate the score using the imported function
            result = evaluate_score(score)
            # Write the result to the file
            file.write(f"{score} is {result}\n")

    print(f"Results have been written to results.txt for {num_scores} scores.")

# Standard way to start the program
if __name__ == "__main__":
    main()
