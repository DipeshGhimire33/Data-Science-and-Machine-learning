
class Access_modifier_Example():
    def __init__(self):
        self.public_attr = 1
        self.__private_attr = 2
        self._protected_attr = 3
        
    def public(self):
        print("Public method") 
    
    def __private(self):
        print("Private method")
    
    def _protected(self):
        print("Protected method")
    
obj = Access_modifier_Example()

obj.public()
# obj.__private()
obj._protected()