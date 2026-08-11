def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(8))

cache = { 0: 0, 1: 1}

def fib(n):
    if n in cache:
        return cache[n]
    else:
        res = fib(n-1)+fib(n-2)
        cache[n]= res
        return res

print(fib(15))


def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

print(fac(5))



