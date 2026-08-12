
class Animal():
    def __init__(self, name : str , age : int):
        self.name = name
        self.age = age
        
    def intro(self):
        print(f"Hello, I am {self.name}")
        
class Cat(Animal):
    def __init__(self,name : str, age : int, color : str):
        super().__init__(name,age)
        self.color = color
    
    def details(self):
        print(f"Hello, I am {self.name} with age: {self.age} and color: {self.color}")
        
cat1 = Cat("Ruby",5,"Purple")
cat1.intro()
cat1.details()