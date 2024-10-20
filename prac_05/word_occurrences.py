"""
Word Occurrences
Estimate: 25 minutes
Actual: 20 minutes
"""

def main():
    word_to_count = {}
    text = input("Text: ")
    words = text.split()

    # Count the occurrences of each word
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Sort the words alphabetically
    sorted_words = sorted(word_to_count.keys())

    # Find the longest word for formatting
    max_length = max(len(word) for word in sorted_words)

    # Print the words and their counts, formatted nicely
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_to_count[word]}")

if __name__ == "__main__":
    main()
