import re

string = "What will happen if a quick brown fox jumps over the gray lazy dog"

pattern = r"brown"

match = re.search(pattern, string)

if match:
    print("Match Start:", match.start())
    print("Match End:", match.end())
    