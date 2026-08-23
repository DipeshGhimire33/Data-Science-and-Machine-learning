def number_generator(start,end):
    for num in range(start,end):  # noqa: UP028
        yield num  
        
gen = number_generator(4,10)

for i in gen:
    print(i)