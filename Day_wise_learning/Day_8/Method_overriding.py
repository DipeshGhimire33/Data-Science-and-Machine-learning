class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        return f"Hello I am {self.name}"
        
    def speak(self):
        return "I can speak"

class Cat(Animal):
    def speak(self):
        return "meow"

cat1 = Cat("Rose", 7)
print(cat1.speak())