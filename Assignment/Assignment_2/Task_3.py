import random

random_number = random.randint(1,100)
print("Welcome to number guessing game.")
print("You get seven chance to guess a no between 1 and 100.")
conf=input("Do you want to play (y/n):")

if conf == "y":
    for i in range(7):
        user_guess=int(input("enter your guess no between 1 and 100: "))
        if user_guess == random_number:
            print("Wow!! You guessed number correctly")
            break
        elif user_guess > random_number:
            print("Oh no !! The number is lower than that")
        else:
            print("Oh no !! The number is higher than that")
    print("Thank you for participating")
