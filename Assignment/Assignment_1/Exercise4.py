# # Exercise 4: Code Completion (String & List Manipulations)
# # Fill in the blanks ___ to transform the user data correctly.
# # Given input string of comma-separated tags with irregular spacing
# tags_input = " python , data-science,
# machine-learning "

# # 1. Split the string into a list of strings by comma
# raw_list = tags_input.___(",")

# # 2. Extract only the first tag and clean surrounding whitespace
# first_tag = raw_list[0].___()

# # 3. Replace hyphens with spaces in the second tag
# second_tag_clean = raw_list[1].strip().___("-", " ")

# # 4. Create a new list combining the cleaned tags using list slicing and replacement
# cleaned_tags = [first_tag, second_tag_clean]

# # 5. Add the last tag (cleaned) to the end of cleaned_tags list
# last_tag_clean = raw_list[-1].strip()
# cleaned_tags.___ (last_tag_clean)

# print(cleaned_tags)
# # Expected output: ['python', 'data science', 'machine-learning']


# ====> Exercise 4 Soln,

tags_input = " python , data-science,machine-learning "
raw_list = tags_input.split(",")
first_tag = raw_list[0].strip()
second_tag_clean = raw_list[1].strip().replace("-"," ")
cleaned_tags = [first_tag, second_tag_clean]

last_tag_clean = raw_list[-1].strip()
cleaned_tags.append(last_tag_clean)

print(cleaned_tags)