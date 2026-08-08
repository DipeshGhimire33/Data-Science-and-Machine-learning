# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".

a="Fizz"
b="Buzz"

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(a+b)
    elif i % 3 == 0:
        print(a)
    elif i % 5 == 0:
        print(b)