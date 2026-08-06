# # Exercise 3: Bug-Fixing (List Mutation & String Slicing)
# # This script is supposed to clean up a list of usernames and format a display title, but it has 3 bugs. Find and ﬁx them.
# raw_title = "PYTHON programming course"

# # Bug 1: Strings are immutable, but the programmer tried to fix formatting in-place
# raw_title.strip()
# raw_title.title()
# print(f"Title: '{raw_title}'")

# # Expected: 'Python Programming Course'

# users = ["alice", "bob", "charlie"]
# # Bug 2: The programmer tried to copy the list, but both variables point to the same list!
# updated_users = users
# updated_users.append("david")
# print(f"Original users: {users}")
# print(f"Updated users: {updated_users}")
# # Expected: ['alice', 'bob', 'charlie']
# # Expected: ['alice', 'bob', 'charlie', 'david']
# # Bug 3: Reverse the title string using slicing
# # The programmer wrote step 1 instead of -1

# reversed_title = raw_title[::-1] # Hint: Look closely at why this isn't printing expected output if raw_title wasn't modified above!


# ====> Exercise 3 soln,

raw_title = "PYTHON programming course"
raw_title.strip()
raw_title.title()
print(f"Title: {raw_title}")

users = ["alice", "bob", "charlie"]
updated_users = users.copy()
updated_users.append("david")
print(f"Original users: {users}")
print(f"Updated users: {updated_users}")

reversed_title = raw_title[::-1]
print(reversed_title)
