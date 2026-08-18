# Calculate the mean and median of a given dataset.

data = [1, 15, 32, 45, 8, 66, 74, 34, 66, 95, 15]

data.sort()

n = len(data)
mean = sum(data) / n


# Calculate the median.

if n % 2 != 0:
    middle_index = n // 2
    median = data[middle_index]
else:
    middle_index = n // 2
    median = (data[middle_index - 1] + data[middle_index]) / 2


print("Mean:", mean)
print("Median:", median)