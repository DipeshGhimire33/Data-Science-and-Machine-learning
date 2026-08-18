import random

print(random.randint(1, 6))

print(random.uniform(1, 6))

print(random.randrange(100, 600, 5))


suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

ranks = list(range(1, 11))
ranks.extend(["Jack", "Queen", "King"])

for _ in range(52):
    print(f"{random.choice(suits)}, {random.choice(ranks)}")