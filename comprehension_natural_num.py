# how to print the sum of first n natural numbers using recursion and list comprehension


n=50

def x(i):
    if i == 0:
        return n
    else:
        return i + x(i - 1)


x=[x(i) for i in range(n)]
print(x[n-1])  # Printing the sum of first n natural numbers using recursion

print(n*(n+1)/2)



