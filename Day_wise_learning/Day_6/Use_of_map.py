# Using map() with a function.


def get_cube(number):
    """Return the cube of a number."""
    return number ** 3


numbers = [1, 2, 9, 3, 5]

cube_values = map(get_cube, numbers)

print(list(cube_values))