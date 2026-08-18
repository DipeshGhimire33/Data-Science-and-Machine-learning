# Using reduce() to calculate the sum of a list.


from functools import reduce


def add(first, second):
    """Return the sum of two numbers."""
    return first + second


numbers = [1, 5, 99, 4, 7, 6]

result = reduce(add, numbers)

print(result)