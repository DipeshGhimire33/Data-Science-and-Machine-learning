# Using enumerate() with a list.

names = ["Ramesh", "Suresh", "Dipesh"]

for index, name in enumerate(names):
    print(index, name)


# Using enumerate() with a dictionary.

marks = {
    "Ramesh": 115,
    "Suresh": 136,
    "Dipesh": 603,
}

print(marks)

print(list(enumerate(marks.items())))