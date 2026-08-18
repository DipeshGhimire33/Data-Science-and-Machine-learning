# Set examples.

first_set = {1, 2, 3, 4, 5, 6}
print(first_set)

second_set = {1, 2, 3, 6, 7, 8, 9}
print(second_set)  # Duplicate values are automatically removed.


# Operations on sets.

first_set = {1, 2, 3, 4, 5, 6}
second_set = {4, 5, 6, 7, 8, 9}

print("Union:", first_set.union(second_set))
print("Intersection:", first_set.intersection(second_set))
print("Difference:", first_set.difference(second_set))
print("Difference:", second_set.difference(first_set))
print(
    "Symmetric difference:",
    first_set.symmetric_difference(second_set),
)
print(
    "Symmetric difference:",
    second_set.symmetric_difference(first_set),
)

print("First set is a subset:", first_set.issubset(second_set))
print("Second set is a subset:", second_set.issubset(first_set))


# Adding and removing elements from a set.

first_set.add(10)
print("After adding 10:", first_set)

second_set.remove(9)
print("After removing 9:", second_set)


# Dictionary examples.

person = {
    "name": "John",
    "age": 25,
    "city": "New York",
}

print(person)


# Adding a new key-value pair.

person["country"] = "USA"
print(person)


# Accessing a value.

print(person["name"])


# Updating a value.

person["age"] = 26
print(person)


# Removing a key-value pair.

person.pop("city")
print(person)


# Incrementing a value.

person["age"] += 1
print(person)


# Tuple examples.
# Tuples are immutable, meaning their elements cannot be changed.

numbers = (1, 2, 3, 4, 5)
print(numbers)


# Accessing an element of a tuple.

print(numbers[0])


# Adding two tuples.

other_numbers = (6, 7, 8, 9, 10)
print(numbers + other_numbers)