import string
from collections import Counter

# File path (same folder as this Python file)
file_path = "sample-file.txt"

# Read file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Split into tokens/ words
tokens = text.split()

clean_tokens = []

for token in tokens:
    # Convert to lowercase
    token = token.lower()

    # Remove punctuation from beginning and end
    token = token.strip(string.punctuation)

    # Keep tokens with at least two alphabetic characters
    alpha_count = sum(char.isalpha() for char in token)
    if alpha_count >= 2:
        clean_tokens.append(token)

# Count word frequencies
word_counts = Counter(clean_tokens)

# Print 10 most frequent words
for word, count in word_counts.most_common(10):
    print(f"{word} -> {count}")
