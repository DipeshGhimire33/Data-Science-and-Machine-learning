# Finding the mode using Counter.

from collections import Counter

data = [1, 15, 32, 15, 45, 8, 66, 15, 74, 34, 66, 95, 15]

frequency = Counter(data)

most_frequent, count = frequency.most_common(1)[0]

print(f"Mode: {most_frequent}")
print(f"Frequency: {count}")


# Finding all modes using the statistics module.

import statistics

data = [1, 15, 32, 45, 8, 66, 74, 34, 66, 95, 15]

modes = statistics.multimode(data)

print(f"Mode(s): {modes}")


# Finding the mode without using libraries.

data = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]

frequency = {}

for number in data:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Frequency:", frequency)

highest_frequency = max(frequency.values())

mode = next(
    number
    for number, count in frequency.items()
    if count == highest_frequency
)

print("Mode:", mode)