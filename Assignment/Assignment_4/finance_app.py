import finance_tool

car_cost = int(input("Enter the cost of car:"))
tax_incurred = finance_tool.calculate_tax(car_cost)
cost_with_tax = car_cost + tax_incurred
print(f"Your total cost is : {cost_with_tax}")

confirmation = input("Do you want a loan? (y/n):")
if confirmation.lower() == "y":
    emi = finance_tool.calculate_emi(cost_with_tax)
    print(f"Your monthly emi would be: {emi} for 12 months")