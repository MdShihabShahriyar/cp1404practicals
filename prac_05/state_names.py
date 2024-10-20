"""
CP1404/CP5632 Practical
State names in a dictionary
File has been reformatted and state inputs can be any case
"""

# PEP 8 formatting for dictionary
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Function to print all states neatly lined up
def print_states(states):
    for code, name in states.items():
        print(f"{code:3} is {name}")

# Print all state codes and names
print_states(CODE_TO_NAME)

# Input state code from user
state_code = input("Enter short state: ").upper()  # Convert input to uppercase
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")  # Access state name using the dictionary
    except KeyError:
        print("Invalid short state")  # Handle case where state code is not found
    state_code = input("Enter short state: ").upper()  # Convert input to uppercase
