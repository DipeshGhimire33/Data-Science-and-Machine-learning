from abc import ABC, abstractmethod

class Vehicle():
    def __init__(self,vehicle_id,brand,rental_price,rental_day = 1):
        self.v_id = vehicle_id
        self.b = brand
        self.__r = rental_price
        self.r_d = 1
        
    @abstractmethod
    def vehicle_details(self):
            print(
                f"The vehicle id is {self.v_id}"
                f"The brand is {self.b}"
                f"The rent is {self.__r}"
            )
            
    def get_rent(self):
        return self.__r
    
    def set_rental_day(self, val):
        self.r_d = val
    
    def get_rental_day(self):
        return self.r_d

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, rental_price,number_of_doors):
        super().__init__(vehicle_id, brand, rental_price)
        self.nod = number_of_doors
        
    def vehicle_details(self):
        print(
            f"The vehicle id is {self.v_id}"
            f"The brand is {self.b}"
            f"The no of doors is {self.nod}"
        )
        
    
class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, rental_price, bike_type):
        super().__init__(vehicle_id, brand, rental_price)
        self.bt = bike_type
        
    def vehicle_details(self):
            print(
                f"The vehicle id is {self.v_id}",
                f"The brand is {self.b}",
                f"The bike type is {self.bt}"
            )
    

bike1 = Bike("1xab", "Yamaha", 500, "Mountain")
bike1.vehicle_details()

def total_rental_cost(bike : Bike):
    total_cost = bike.get_rent() * bike.get_rental_day()
    print(total_cost)

bike1.set_rental_day(15)
total_rental_cost(bike1)
