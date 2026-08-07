# practice Day 2 for file writing and extracting singular content from it and performing conditional check.

file = open("practice.txt", mode="w")
file.write("This is an practice task of day 2.\n In this we will try to write contents in a file. \n We will extract each words  then count the total no of vowels and consonents in the text.")
file.close()

count_vow=0
count_con=0

with open("practice.txt", mode ="r") as file:
    for line in file:
        x=line.split()
        
        for i in x:
            
            for j in i:
                j.lower()
                
                if j == "a" or j == "e" or j == "i" or j == "o" or j == "u" : 
                    count_vow = count_vow + 1
                else:
                     count_con = count_con + 1

print(count_vow)               
print(count_con)               