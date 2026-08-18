# Sorting a list of data based on ID and address.

raw_data = [
    ["15", "Ram", "Kathmandu"],
    ["10", "Shyam", "Biratnagar"],
    ["20", "Kiran", "Jhapa"],
    ["1", "Isha", "Bhaktapur"],
]


# Sort by ID using sorted().
sorted_data = sorted(raw_data, key=lambda person: int(person[0]))

print("Sorted by ID:")
print(sorted_data)


# Sort by address using sort().
raw_data.sort(key=lambda person: person[2])

print("Sorted by address:")
print(raw_data)