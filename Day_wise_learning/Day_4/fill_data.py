# Fill missing values in raw data.

raw_data = [
    ["Ram", "10", ""],
    ["Shyam", "12", "Kathmandu"],
    [" ", "15", "Bhaktapur"],
]

filled_data = []

for person in raw_data:
    name = person[0].strip()
    age = person[1].strip()
    address = person[2].strip()

    if name and age and address:
        filled_data.append(person)

    elif name and age:
        person[2] = "Kathmandu"
        filled_data.append(person)

    elif name and address:
        person[1] = "18"
        filled_data.append(person)

    elif age and address:
        person[0] = "No name"
        filled_data.append(person)

print(filled_data)