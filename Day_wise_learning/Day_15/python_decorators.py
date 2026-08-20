#Example
class Test:
    
    @staticmethod
    def something():
        print("Hello")

    something()
# Implementation

def decorator(func):
    def wrapper():
        
        print("before function call")
        print(func().upper())
        print("After Function Call")
        
    return wrapper

@decorator
def greet():
    return "hello world"

greet()
