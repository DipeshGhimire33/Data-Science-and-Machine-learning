def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, "r") as file:
        print(file.read())

write_to_file("greetings.txt", "Hello, Python!")
read_from_file("greetings.txt")