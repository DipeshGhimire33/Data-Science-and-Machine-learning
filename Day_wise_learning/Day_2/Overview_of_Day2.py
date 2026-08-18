# Practice Day 2:
# Write content to a file and count vowels and consonants.

with open("practice.txt", mode="w") as file:

    file.write(
        "This is a practice task for Day 2.\n"
        "In this task, we will write content to a file.\n"
        "We will extract each word and count the total number "
        "of vowels and consonants in the text."
    )




vowel_count = 0
consonant_count = 0

with open("practice.txt", mode="r") as file:
    for line in file:
        words = line.split()

        for word in words:
            for character in word.lower():
                if character in "aeiou":
                    vowel_count += 1
                elif character.isalpha():
                    consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)