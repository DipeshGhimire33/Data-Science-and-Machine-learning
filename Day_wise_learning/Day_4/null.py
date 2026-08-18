# Select records with complete data.

raw_data = [
    ["Ram", "10", ""],
    ["Shyam", "12", "Kathmandu"],
    [" ", "15", "Bhaktapur"],
]

clean_data = []

for person in raw_data:
    name = person[0].strip()
    age = person[1].strip()
    address = person[2].strip()

    if name and age and address:
        clean_data.append(person)

print(clean_data)