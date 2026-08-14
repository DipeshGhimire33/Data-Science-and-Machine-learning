from abc import ABC, abstractmethod

class Shape(ABC):
    
    def __init__(self,length,bredth = 0,height = 0):
        self.length = length
        self.bredth = bredth
        self.height = height
        
    
    @abstractmethod
    def area(self):
        pass
    
    def volume(self):
        return "Shape not applicable"
    
class Rectangle(Shape):
    def area(self):
        return self.length*self.bredth
    
rect = Rectangle(15,20)
print(rect.area())
print(rect.volume())

class Cube(Shape):
    def area(self):
        return 2*(self.length*self.bredth + self.bredth*self.height + self.height*self.length)
        
    
cub = Cube(15,20,15)
print(cub.area())
    
import math

class Circle(Shape):
    def __init__(self,radius):
        self.r = radius
    
    def area(self):
        return math.pi * (self.r**2)  

circ = Circle(5)
print(round(circ.area(),2))  