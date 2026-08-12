
class Student():
    
    def __init__(self,name : str ,*marks : int):
        self.name = name
        self.marks = marks
        
    def total(self):
        return sum(self.marks)
        
    def average(self):
        total_ = self.total()
        return total_/ len(self.marks)
        
    def display(self):
        print(f"Name is {self.name}")
        print(f"Total Marks is {self.total()}")
        print(f"Average is {self.average()}")

student1 = Student("Dipesh",60,70,80)
student1.display()
