# basic multi_level inheritance
class Grandfather():
    def g_says(self):
        print("I am your fathers dad")
        
class Father(Grandfather):
    def f_says(self):
        print("I am your father")

class Child(Father):
    def c_says(self):
        print("I am a child")
        
child1 =Child()
child1.c_says()
child1.f_says()
child1.g_says()


# Operation 

class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
class Employee(Person):
    def __init__(self,name,age, employeeID):
        super().__init__(name,age)
        self.employeeID = employeeID

class Manager(Employee):
    def __init__(self,name,age,employeeID, department):
        super().__init__(name,age,employeeID)
        self.department = department
    
    def intro(self):
        print(self.name,self.age,self.employeeID,self.department)
        
manager1 =Manager("Ram",50,15,"finance")
manager1.intro()