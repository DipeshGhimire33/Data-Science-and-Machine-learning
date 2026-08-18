# Lists within a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

nested_numbers = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 0],
]


# Iterating through a normal list.

for number in numbers:
    print(number)


# Iterating through a nested list.

for pair in nested_numbers:
    print(pair)


# Iterating through each element of a nested list.

for pair in nested_numbers:
    for number in pair:
        print(number)


# Accessing an element from a nested list.

print(nested_numbers[0][1])