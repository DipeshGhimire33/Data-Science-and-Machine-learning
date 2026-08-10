# to calculate standard deviation from the given list of numbers

def std_calc(*numbers):
    N =len(numbers)
    mean = sum(numbers)/N
    numerator=sum((number -mean)**2 for number in numbers)
    std= (numerator/N)**0.5
    return std

print(round(std_calc(1,5,6,7,6,9,1.5,93,4),2))