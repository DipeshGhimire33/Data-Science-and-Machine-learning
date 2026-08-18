# Create a dictionary of words longer than four characters
# and their lengths.

sentence = "Hello, how are you doing today?"
word_lengths = {}

for word in sentence.split():
    if len(word) > 4:
        word_lengths[word] = len(word)

print(word_lengths)


# Create a set of unique letters in the sentence.

letters = {character for character in sentence if character.isalpha()}

print(letters)


# Clean and filter numeric data.

raw_data = [
    "150",
    "invalid",
    "400",
    "80",
    "300",
    "error",
    "250",
    "999",
    "1500",
]

cleaned_data = [
    int(value)
    for value in raw_data
    if value.isdigit() and 150 <= int(value) <= 999
]

print(cleaned_data)