import time

print(time.time())

print(time.ctime())

print(time.gmtime())

print(time.localtime())


start = time.time()

print("function started")

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

print(fac(150)) # max 996 depth

print("function Ended")

end = time.time()

print(end - start)