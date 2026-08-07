# Python
# Input matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Expected Output: [4, 16, 36, 64]
# Your code here:
y=[]
for i in matrix:
    for j in i:
        if j%2==0:
            y.append(j**2)

print(y)
