# reduce()

from functools import reduce

def add(x,y):
    return x+y

my_list=[1,5,99,4,7,6]
res = reduce(add,my_list)