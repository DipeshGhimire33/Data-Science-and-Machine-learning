test_numbers = [
    -10, -1, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 15, 17, 19,
    21, 25, 27, 47, 49, 79, 97, 100, 523, 527, 1000, 7919,
    10000, 104729, 1000000
]


def is_prime(n):
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


prime = []
composite = []
neither = []

for n in test_numbers:
    if n < 2:
        neither.append(n)
    elif is_prime(n):
        prime.append(n)
    else:
        composite.append(n)

print("Prime:", prime)
print("Composite:", composite)
print("Neither:", neither)