
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __len__(self):
        return 2
    
    def __add__(self, other):
        new_x =self.x + other.x
        new_y =self.y + other.y
        return Point(new_x,new_y)
    
    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        return Point(new_x,new_y)
    
    def quad(self):
        if not self.x and not self.y :
             return "origin"
        elif not self.x or not self.y:
            return "axis"
        elif self.x > 0 and self.y > 0: 
            return "first"
        elif self.x < 0 and self.y > 0:
            return "second"
        elif self.x < 0 and self.y < 0:
            return "third"
        else :
            return "fourth"
        
    def quad_teach(self):
        if not self.x and not self.y :
            return "origin"
        elif not self.x or not self.y:
            return "axis"
        quardent_mapp = {
            (True,True) : "first",
            (False,True) : "second",
            (False,False) : "third",
            (True,False) : "fourth"
        }
        return quardent_mapp.get((self.x > 0,self.y > 0))
            
p1 = Point(5,4)
p2 = Point(5,4)

p3 = p1 + p2
print(p3)

p4 = p1*p2
print(p4)
p5 = Point(0,1)

print(p1.quad())
print(p5.quad_teach())