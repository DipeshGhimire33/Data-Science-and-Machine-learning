import os

if os.path.exists("test"):
    print("hi")
else:
    print("bye")

if os.path.exists("Day_wise_learning/Day_20"):
    print("hi")
else:
    os.mkdir("Day_wise_learning/Day_20")
    
print(os.listdir())

print(os.environ)