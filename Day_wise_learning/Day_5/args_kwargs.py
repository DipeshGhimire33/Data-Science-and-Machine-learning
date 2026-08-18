def print_all(*args):
    """Return all positional arguments as a tuple."""
    print("Arguments:")
    return args


print(print_all(1, 5, "hi", 3, 4))


def sum_all(*numbers):
    """Return the sum of all positional arguments."""
    return sum(numbers)


print(sum_all(1, 5, 4.6, 32, 0.55))


def print_kwargs(**kwargs):
    """Print all keyword arguments as a dictionary."""
    print("Keyword arguments:")
    print(kwargs)


print_kwargs(num1=1, num2=5)


def calculate_area(shape: str, **kwargs):
    """Calculate the area of a supported shape."""
    if shape == "square":
        return kwargs.get("length", 0) ** 2

    if shape == "rectangle":
        if "length" in kwargs and "breadth" in kwargs:
            return kwargs["length"] * kwargs["breadth"]

        print("Length and breadth are required.")
        return 0

    print(f"{shape} is not supported.")
    return 0


print(calculate_area("rectangle", length=15, breadth=20))