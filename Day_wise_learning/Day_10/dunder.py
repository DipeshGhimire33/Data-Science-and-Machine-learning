
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def  __str__(self):
        return f"{self.name}/{self.age}"
    
    def __repr__(self):
        return f"Hi {self.name}"
    
    def __len__(self):
        return self.age
    
    def __call__(self, gender = "male"):
        return gender
    
person = Person("Ram", 55)
print(person)
print(repr(person))
# print(person.__len__())
print(len(person))
print(person.__call__())




        