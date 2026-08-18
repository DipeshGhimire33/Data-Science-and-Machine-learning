# Adding corresponding elements of two lists.

first_list = [1, 2, 3, 4]
second_list = [5, 6, 7, 8]

sum_list = [0] * len(first_list)

for i in range(len(first_list)):
    sum_list[i] = first_list[i] + second_list[i]

print("Sum:", sum_list)


# Subtracting corresponding elements of two lists.

first_list = [15, 20, 25, 30]
second_list = [5, 10, 15, 20]

difference_list = [0] * len(first_list)

for i in range(len(first_list)):
    difference_list[i] = first_list[i] - second_list[i]

print("Difference:", difference_list)