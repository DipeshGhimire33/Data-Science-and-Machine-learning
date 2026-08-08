# Armstrong number in python

num = input ( " Enter a number to check if Armstrong or not : ")
s=0
for i in num:
   s=int(i)**len(num)+s

if str(s) == num:
   print(f"{num} is armstrong")
else:
   print(f"{num} is not an armstrong no")








