# Calculate the population standard deviation of given numbers.


def calculate_standard_deviation(*numbers):
    """Return the population standard deviation of the given numbers."""
    count = len(numbers)
    mean = sum(numbers) / count

    squared_differences = sum(
        (number - mean) ** 2 for number in numbers
    )

    return (squared_differences / count) ** 0.5


result = calculate_standard_deviation(1, 5, 6, 7, 6, 9, 1.5, 93, 4)

print(round(result, 2))