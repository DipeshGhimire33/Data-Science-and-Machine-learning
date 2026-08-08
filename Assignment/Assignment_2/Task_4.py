# Armstrong number in python using String as input

num = input ( " Enter a positive number to check if Armstrong or not : ")
# num=num.strip("-")                    # for forcing the string to not have "-" sign
s=0
for i in num:
   s=int(i)**len(num)+s

if str(s) == num:
   print(f"{num} is armstrong")
else:
   print(f"{num} is not an armstrong no")

# Armstrong number in python using integer as input

num = int ( input ( "enter a positive no :"))
s=0
for i in str(num):
   s= int(i) ** len(str(num)) + s

if s == num:
   print(f"{num} is an armstrong")
else:
   print(f"{num} is not an armstrong no")
   





