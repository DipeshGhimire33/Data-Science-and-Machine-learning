# Write and Read operations within a file

file=open("Day2.txt", mode="w")
file.write("This is Day 2 of basic python learning. \n")
file.write("We are currently performing File Operations.")
file.close()

file = open("Day2.txt", mode="r")
print(file.read())
file.close()

