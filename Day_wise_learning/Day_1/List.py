# Basic list operations in Python.

numbers = [1, 2, 3, 4, 5]

# Iterating through a list.
for number in numbers:
    print(number)


# List slicing.
print(numbers[:-1])    # All elements except the last one.
print(numbers[1:])     # All elements except the first one.
print(numbers[1:-1])   # All elements except the first and last ones.


# Copying a list.
copied_numbers = numbers.copy()
copied_numbers.append(6)


# Referencing the same list.
referenced_numbers = numbers
referenced_numbers.append(7)

print("Original list:", numbers)
print("Copied list:", copied_numbers)
print("Referenced list:", referenced_numbers)


# List concatenation and repetition.
other_numbers = [1, 2, 3, 4, 5]

print("Concatenated lists:", numbers + other_numbers)
print("Repeated list:", numbers * 2)
print("Length of list:", len(numbers))


# Lists cannot be subtracted or multiplied by another list.
# print(numbers - other_numbers)  # TypeError
# print(numbers * other_numbers)  # TypeError