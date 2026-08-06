# Using context manager to reduce manual closing

with open("Day2.txt", mode="a+") as file:
    file.write("\n Hey this is Context manager")

with open("Day2.txt",mode="r")as file:
    print(file.read())
print("Closed")