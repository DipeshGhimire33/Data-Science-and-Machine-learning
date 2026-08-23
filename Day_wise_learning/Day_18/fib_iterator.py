

class Fibonacci:
    def __init__(self, limit = 10):
        self.limit = limit
        
        self.step = 0
        
        self.current = 0
        self.next = 1        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.step >= self.limit:
            raise StopIteration
        
        result = self.current
        self.current, self.next = self.next, self.current+ self.next
        
        self.step += 1
        
        return result
    
    def __len__(self):
        return self.limit
    
fib = Fibonacci(3)

for i in fib:
    print(i)
    
print(len(fib))
        