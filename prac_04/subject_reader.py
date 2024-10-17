"""
CP1404/CP5632 Practical Suggested Solution
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    """Read subject data and display neatly."""
    subjects = load_subjects()  # Load data from file
    display_subjects(subjects)  # Display the data


def load_subjects():
    """Load data from file formatted like: code,lecturer,number_of_students."""
    subjects = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove any trailing newline characters
            parts = line.split(',')  # Split the line into parts by comma
            parts[2] = int(parts[2])  # Convert the number of students to an integer
            subjects.append(parts)  # Append the list to the subjects list
    return subjects


def display_subjects(subjects):
    """Display data nicely."""
    for subject in subjects:
        # Format and display each subject's information
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
