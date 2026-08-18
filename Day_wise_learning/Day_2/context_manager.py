# Using a context manager to handle file closing automatically.

with open("Day2.txt", mode="a+") as file:
    file.write("\nHey, this is a context manager.")

with open("Day2.txt", mode="r") as file:
    print(file.read())

print("File closed automatically.")