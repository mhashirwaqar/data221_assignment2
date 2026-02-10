import string
from collections import Counter

# File path (same folder as this Python file)
file_path = "sample-file.txt"

# Read file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Split into tokens
tokens = text.split()

clean_tokens = []

# Clean tokens
for token in tokens:
    token = token.lower()
    token = token.strip(string.punctuation)

    # Keep tokens with at least two alphabetic characters
    alpha_count = sum(char.isalpha() for char in token)
    if alpha_count >= 2:
        clean_tokens.append(token)

# Construct bigrams (pairs of consecutive words)
bigrams = []

for i in range(len(clean_tokens) - 1):
    bigram = (clean_tokens[i], clean_tokens[i + 1])
    bigrams.append(bigram)

# Count bigram frequencies
bigram_counts = Counter(bigrams)

# Print 5 most frequent bigrams
for bigram, count in bigram_counts.most_common(5):
    print(bigram[0], bigram[1], "->", count)
