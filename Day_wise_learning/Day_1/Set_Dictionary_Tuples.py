# SET Examples

a={1,2,3,4,5,6}
print(a)  # Printing the set a

x={1,2,3,6,6,7,8,9}
print(x)  # Printing the set x, which will automatically remove duplicates

# Operations on sets
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}

print(a.union(b))  # Printing the union of sets a and b
print(a.intersection(b))  # Printing the intersection of sets a and b
print(a.difference(b))  # Printing the difference of sets a and b
print(b.difference(a))  # Printing the difference of sets b and a
print(a.symmetric_difference(b))  # Printing the symmetric difference of sets a and b A' + B' = (A - B) U (B - A)
print(b.symmetric_difference(a))  # Printing the symmetric difference of sets b and a B' + A' = (B - A) U (A - B)
print(a.issubset(b))  # Checking if set a is a subset of set b
print(b.issubset(a))  # Checking if set b is a subset of set a

# Adding and removing elements from a set
a.add(10)  # Adding an element to the set a
print(a)  # Printing the updated set a

b.remove(9)  # Removing an element from the set b
print(b)  # Printing the updated set b


# Dictionary Examples

a={'name':'John', 'age':25, 'city':'New York'}
print(a)  # Printing the dictionary a

# Adding a new key-value pair to the dictionary
a['country']='USA'  # Adding a new key-value pair to the dictionary a
print(a)  # Printing the updated dictionary a

print(a['name'])  # Accessing the value associated with the key 'name' in the dictionary a

a['age'] = 26  # Updating the value associated with the key 'age' in the dictionary a
print(a)  # Printing the updated dictionary a   

a.pop('city')  # Removing the key-value pair with the key 'city' from the dictionary a
print(a)  # Printing the updated dictionary a after removing the key-value pair with the key

a['age'] = a['age'] + 1  # Updating the value associated with the key 'age' in the dictionary a
print(a)  # Printing the updated dictionary a after incrementing the value associated with the key 'age'

# Tuples Examples ( Immutable/Non-changable objects in Python)

a=(1,2,3,4,5)
print(a)  # Printing the tuple a

# Accessing elements of a tuple
print(a[0])  # Accessing the first element of the tuple a

# Operations on tuples

# Addition of two tuples
b=(6,7,8,9,10)
print(a + b)  # Printing the result of adding tuples a and b

# Basic use of Set , Dictionary and Tuples.