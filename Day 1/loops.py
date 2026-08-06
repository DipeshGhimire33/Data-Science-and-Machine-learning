# Basic introduction to loops in Python

# 1.For loop

for i in range(5):            #range(5) will generate numbers from 0 to 4
    print(i)

#2. While loop

a=5
while a>0:
    print(a)
    a-=1

#3. Nested loop

for i in range(3):
    for j in range(2):
        print(i, j)          #prints the values like (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)