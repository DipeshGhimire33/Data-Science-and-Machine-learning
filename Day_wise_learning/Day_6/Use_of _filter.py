# Using filter() with lambda functions.

numbers = [1, 2, 9, 3, 5]

# Filter even numbers.
even_numbers = filter(lambda number: number % 2 == 0, numbers)

print(list(even_numbers))


# Filter odd numbers.
odd_numbers = filter(lambda number: number % 2 != 0, numbers)

print(list(odd_numbers))