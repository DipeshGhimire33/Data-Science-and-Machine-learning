# # Performing various Basic simple programs

# # Basic Input and Output
print("Hello user please enter your name:")
name = input()
print("Hello " + name + "! Welcome to the program.")
print("Please enter your age:")
age = input()

con = "no"
while con != "yes":
    con=input("Are you sure you are " + age + " years old? (yes/no)")
    if con == "yes":
        print("Great! Let's continue.")
        print("your name is " + name + " and your age is " + age + ".")
    else:
        age=input("Please enter your age again:")



# Basic Temperature Conversion
conf="yes"

while conf == "yes":
    Options = input("Please select the conversion you want to perform:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n 3. Celsius to Kelvin \n 4. Kelvin to Celsius\n 5.Faherenheit to Kelvin \n 6. Kelvin to Faherenheit \nEnter 1, 2, 3, 4, 5 or 6: ")
    if Options == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif Options == "2":
        fahrenheit = float(input("Enter Temperature in Fahrenheit:"))   
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    elif Options == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C is equal to {kelvin:.2f}K")
    elif Options == "4":
        kelvin = float(input("Enter Temperature in Kelvin:"))
        celsius = kelvin - 273.15
        print(f"{kelvin}K is equal to {celsius:.2f}°C")
    elif Options == "5":
        fahrenheit = float(input(" Enter Temperature in Fahrenheit:"))
        kelvin = ((fahrenheit - 32)* 5/9) + 273.15
        print(f"{fahrenheit}°F is equal to {kelvin:.2f}K")
    elif Options == "6":
        kelvin = float(input("Enter Temperature in Kelvin:"))
        fahrenheit=((kelvin -273.15)*9/5)+32
        print(f"{kelvin}K is equal to {fahrenheit:.2f}°F")
    else:
        print("Enter valid options")

    conf=input("Do you want to continue (yes/no):")    


# Calculation of prime numbers 1 to n and presenting it in list

import math

n = int(input("enter a number:"))
x=[]

def prmcheck(i):
    for j in range (2,int(math.sqrt(i))+1):         #for faster prime check
            if i % j == 0:
                return False
    return True


for i in range(2,n+1):
    y = prmcheck(i)
    if y == True:
      x.append(i)   
            
print(x)


# Printing basic structures using loops

for i in range(6):
        print("*"*i)

for i in range(6):
        print(" "*(6-i)+"*"*i)
       
for i in range(6):
        print(" "*(6-i)+"* "*i)                 #giving space after "*"

# Printing data from list in structure

x=[5,32,6,77,64,69,11]
y=[]

for i in x:
    k=i//10
    j=i%10
    if k !=0:
        y.append(k)
        y.append(j)
    else:
        y.append(j)
    print(y)

# each j and k can be structured without list in similar manner to above programs


# Overview of what i learned and applied in python learning Day 1