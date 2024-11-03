"""
CP1404/CP5632 Practical - Client code for ProgrammingLanguage class.

Estimated time: 20 minutes
Current time: [Your current time here]
"""

from programming_language import ProgrammingLanguage

# Creating instances of ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print the string representation of the Python programming language
print(python)

# List of ProgrammingLanguage objects
languages = [python, ruby, visual_basic]

# Print the dynamically typed languages
print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
