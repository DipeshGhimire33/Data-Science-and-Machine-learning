# Fibonacci sequence using basic recursion.


def fibonacci(number):
    """Return the nth Fibonacci number using recursion."""
    if number == 0:
        return 0
    elif number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(8))


# Fibonacci sequence using recursion with memoization.

cache = {
    0: 0,
    1: 1,
}


def fibonacci_cached(number):
    """Return the nth Fibonacci number using memoization."""
    if number in cache:
        return cache[number]

    result = fibonacci_cached(number - 1) + fibonacci_cached(number - 2)
    cache[number] = result

    return result


print(fibonacci_cached(15))


# Factorial using recursion.


def factorial(number):
    """Return the factorial of a positive integer."""
    if number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))