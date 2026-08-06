# Basic use of fuction 

def sum(x):
    z=0
    z=z+x
    return z

n= int(input("enter no of nos you want to add:"))
c=0

for i in range(n):
   x=int(input(f"enter {i+1} no: "))
   c=c+sum(x)

print(c)

# Basic utilization of class

class Calc():
    def __init__(self,length,bredth):               # using same constructor parameters for area and volume
        self.length=length
        self.bredth=bredth

    def area(self):
        return self.length*self.bredth

    def volume(self,h):
        height=h
        return self.length*self.bredth*height

conf=input("Do you want to calculate area or volume? \n ")
conf.lower()
if conf == "area":
    l=int(input("enter length:"))
    b=int(input("enter bredth:"))
    res=Calc(l,b).area()
else:
     l=int(input("enter length:"))
     b=int(input("enter bredth:"))
     h=int(input("enter height:"))
     res =Calc(l,b).volume(h)

print(f"The result is {res}")