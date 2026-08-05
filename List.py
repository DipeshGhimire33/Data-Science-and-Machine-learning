# Basic List operations in Python

a = [1, 2, 3, 4, 5]  # Creating a list
for i in a:
    print(i)  # Printing each element in the list

print(a[:-1])  # Printing all elements except the last one
print(a[1:])  # Printing all elements except the first one
print(a[1:-1])  # Printing all elements except the first and last one

b= a.copy()  # Creating a copy of the list
b.append(6)  # Adding an element to the end of the list

c=a
c.append(7)  # Adding an element to the end of the list

# x=y makes x and y point to the same list in memory, so changes to one will affect the other.

print(a)  # Printing the original list
print(b)  #Printing the copied list
print(c)  # Printing the modified list


d= [1, 2, 3, 4, 5]
print(a+d)  # Concatenating two lists
print(a*2)  # Repeating the list twice
print(len(a))  # Printing the length of the list


#print(a*d)  # This will raise an error because lists cannot be multiplied by other lists in Python
#print(a-d)  # This will raise an error because lists cannot be subtracted in Python