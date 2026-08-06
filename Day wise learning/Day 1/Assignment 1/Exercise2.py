# # Exercise 2: Code Completion (Operator Precedence & Floor Math)
# # Fill in the blanks ___ to make the assertions pass.
# # 1. Complete the formula for compound interest: A = P(1 + r/n)^(nt)
# principal = 1000
# rate = 0.05
# time = 2
# n_compounds = 12

# # Hint: Use parentheses carefully for precedence and the correct exponent operator
# amount = principal * (1 + rate / n_compounds) ___ (n_compounds * time)

# # 2. Get the number of remaining hours after removing full days from a total
# total_hours = 130
# remaining_hours = total_hours ___ 24 # Complete with the correct operator

# # 3. Calculate full 7-day weeks in a total number of days
# total_days = 45
# full_weeks = total_days ___ 7 # Complete with integer division operator

# print(f"Amount: {round(amount, 2)}")
# print(f"Remaining Hours: {remaining_hours}")
# print(f"Full Weeks: {full_weeks}")

# # Expected: 1104.94
# # Expected: 10
# # Expected: 6


# ===> Exercise 2 Soln,

principal = 1000
rate = 0.05
time = 2
n_compounds = 12

amount = principal * (1 + rate / n_compounds)**(n_compounds * time)
total_hours = 130
remaining_hours = total_hours%24
total_days = 45
full_weeks = total_days // 7

print(f"Amount: {round(amount, 2)}")
print(f"Remaining Hours: {remaining_hours}")
print(f"Full Weeks: {full_weeks}")