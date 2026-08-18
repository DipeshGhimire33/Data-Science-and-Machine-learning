# Write and read operations within a file.

with open("Day2.txt", mode="w") as file:
    file.write("This is Day 2 of basic Python learning.\n")
    file.write("We are currently performing file operations.")


with open("Day2.txt", mode="r") as file:
    print(file.read())
