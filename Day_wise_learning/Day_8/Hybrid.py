class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Hello I am {self.name}")

class Cat(Animal):
    def speak(self):
        return "meow"

class Tiger(Cat):
    def speak(self):
        return "Roar"

class Jagwar(Cat):
    def speak(self):
        return "Grrrr"
    
jaguar1 = Jagwar("Wilson",13)
print(jaguar1.speak())