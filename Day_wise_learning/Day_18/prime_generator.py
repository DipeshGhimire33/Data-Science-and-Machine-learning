def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True
        


def prime_generator(limit = 10):
    count, start = 1 , 1
    
    while count <= limit:
        start += 1
        if is_prime(start):
            count += 1
            yield start
    
prime_gen_obj = prime_generator(6)
print(list(prime_gen_obj))