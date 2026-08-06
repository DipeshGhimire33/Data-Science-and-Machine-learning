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


# Data Cleaning and Processing

raw_data=['150', 'invalid', '400','80' '300', 'error', '250','999','1500']

cleaned_data = [int(x) for x in raw_data if x.isdigit() if int(x) >= 150 and int(x)<=999]  # Cleaning the data by filtering out non-numeric values and values less than or equal to 100
print(cleaned_data)  # Printing the list of cleaned numeric values
