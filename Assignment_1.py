# This code snippet processes a given sentence to create a dictionary of words that have more than 4 characters,
#  along with their lengths. It also creates a set of unique letters present in the sentence.

sent="Hello, how are you doing today?"
res = {}
for word in sent.split():
    if len(word) > 4:
        res[word] = len(word) 
    
print(res)  # Printing the dictionary of words with length greater than 4 and their lengths

letters={i for i in sent if i.isalpha()} 
print(letters)  # Printing the set of unique letters in the sentence