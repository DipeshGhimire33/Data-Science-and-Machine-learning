class InvalidAgeException(Exception):
    """ Raise When input age is less than 18 """

def check_customer(age):
    print(int(age))
    if int(age) >= 18:
        
        print("good to go")
    else:
        raise InvalidAgeException("Age should be greter than 18")

customer_id = {"id": "154Axd", "age": "21"}

age = customer_id["age"]   
try:
    check_customer(age)
except (ValueError, TypeError):
    print("Invalid Age")
    
