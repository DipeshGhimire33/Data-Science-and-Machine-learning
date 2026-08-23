class CheckPrime:
    def __init__(self, limit):
        self.limit = limit
        
        self.step = 0
        self.current = 1
        
    
    def __iter__(self):
            return self
      
    def is_prime(self, n):
        if n < 2 :
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False 
        return True
    
    def __next__(self):
            if self.step >= self.limit:
                raise StopIteration  
            
            while True:
                self.current += 1
                if self.is_prime(self.current):
                    self.step += 1
                    return self.current
        
    def __len__(self):
         return self.limit    
        
prime = CheckPrime(10)

print(list(prime))
        
        
        
        