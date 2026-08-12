# instance class satic methods

class Person:
    
    count=0
    
    def __init__(self, name,address : str = "kathmandu"):
        self.name=name
        self.address=address
        Person.count += 1
    
    def get_details(self):
        print(f"I am {self.name} from {self.address}")

    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def get_full_name(first,last):
        print(f"Hello Mr.{last} {first}")
    

person1 = Person("Rujan","Jhapa")
person1.get_details()
person1.get_full_name("Rujan","Katwal")



        