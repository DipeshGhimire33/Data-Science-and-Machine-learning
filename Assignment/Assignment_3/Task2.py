from functools import reduce

transactions = [
    {"id": 101, "amount": 250.0, "status": "completed", "currency": "USD"},
    {"id": 102, "amount": 0.0,   "status": "pending",   "currency": "USD"},
    {"id": 103, "amount": 180.5, "status": "completed", "currency": "USD"},
    {"id": 104, "amount": 45.0,  "status": "refunded",  "currency": "USD"},
    {"id": 105, "amount": 500.0, "status": "completed", "currency": "USD"},
]


completed = [t for t in transactions if t["status"] == "completed"]
# non_completed = [t for t in transactions if t["status"] != "completed"]


amounts = map(lambda t: t["amount"] * 1.1, completed)
total_with_tax = reduce(lambda x, y: x + y, amounts)

print(round(total_with_tax, 2))  
