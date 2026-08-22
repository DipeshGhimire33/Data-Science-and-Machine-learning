import time


class UnderAgeException(Exception):
    
    """
    Class that throws error if age< 18
    """ 
    
def register_user(name: str, age: int):
    
    if age >= 18:
        print(f"Welcome : {name}")
    else:
        raise UnderAgeException
    
try:
    name = input("Enter your name :")
    age = int(input("Enter your age :"))  
    register_user(name, age) 
    print("Wait ... ... ...")
except UnderAgeException:
    time.sleep(2)
    print("User, your age is less than 18. Can't let you register")
finally:
    time.sleep(2)
    print("Thank you for using MovieTime")                                                                        