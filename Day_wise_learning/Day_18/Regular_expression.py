import re

string = "What will happen if a quick brown fox jumps over the gray lazy dog"

pattern = r"brown"

match = re.search(pattern, string)

if match:
    print("Match Start:", match.start())
    print("Match End:", match.end())
    

#1. Check if a string contains a number    

text = "My age is 25"

result = re.search(r"\d+", text)

if result:
    
    print(result.group())
    
#2. Find all words starting with A

text = "Apple Amazon Banana Avocado Orange"

words = re.findall(r"\bA\w*", text)

print(words)

#3 re.split(pattern,string,maxsplit = 0)

pattern = r"\[\d+\]"

segments = re.split(
    pattern,
    "Hello[78], I am wikkipedia[159]"
)

print(segments)  