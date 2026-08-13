class Example():
    def add(self, a,b,c=0):
        return a+b+c

e = Example()
print(e.add(5,4))
print(e.add(5,4,3))
print(e.add("5","4","9"))
print(round(e.add(5.657,4.378),2))

class Example1():
    def add(self,*args):
        return sum(args)

eg = Example1()
print(eg.add(45,68.215,49,45,55.55))