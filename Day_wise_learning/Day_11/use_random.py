import random

print(random.randint(1,6))

print(random.uniform(1,6))

print(random.randrange(100,600,5))

cards = ["Hearts","Spade","Diamond","Club"]
number_card = [i for i in range (1,11)]
number_card.append("Jack")
number_card.append("Queen")
number_card.append("King")
for x in range(52):
    print(f"{random.choice(cards)},{random.choice(number_card)}")