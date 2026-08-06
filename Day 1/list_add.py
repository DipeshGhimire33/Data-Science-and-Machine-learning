# How to add elements of two different list in Python

a=[1, 2, 3, 4]
b= [5, 6, 7,8]
c= [0]*len(a)  # Initializing list c with zeros of the same length as list a

for i in range(len(a)):
    c[i]= a[i] + b[i]  # Adding corresponding elements from list a and b

print(c)  # Printing the result of adding elements from list a and b



# How to subtract elements of two different list in Python

a=[15, 20, 25, 30]
b= [5, 10, 15, 20]

d= [0]*len(a)  # Initializing list d with zeros of the same length as list a

for i in range(len(a)):
    d[i]= a[i] - b[i]  # Subtracting corresponding elements from list a and b

print(d)  # Printing the result of subtracting elements from list a and b