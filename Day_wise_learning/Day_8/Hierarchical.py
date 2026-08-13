
class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Hello I am {self.name}")

class Cat(Animal):
    def speak(self):
        return "meow"
    
class Dog(Animal):
    def speak(self):
        return "woof"
                
cat1 = Cat("Ruby",5)
cat1.intro()
print(cat1.speak())

        