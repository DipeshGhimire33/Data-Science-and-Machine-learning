class Parent1():
    def parent1(self):
        print("this is parent 1")

class Parent2():
    def parent2(self):
        print("this is parent 2")
        
class Parent3():
    def parent1(self):
        print("this is parent 3")
        

class Child(Parent3,Parent2,Parent1):
    def child_of_3(self):
        print("this is child ")

child1 = Child()
child1.parent1()
child1.parent2()
child1.child_of_3()
