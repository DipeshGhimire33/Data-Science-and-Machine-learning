from collections import Counter

data = [1,15,32,15,45,8,66,15,74,34,66,95,15]

count = Counter(data)

# the above program counts frequency if needed for any kind of large statistical data

most_frequent, frequency = count.most_common(1)[0]
print(f"Mode: {most_frequent}")

# if more than one data with high frequency " importing statistics"

import statistics

mult_data = [1,15,32,45,8,66,74,34,66,95,15]
modes = statistics.multimode(mult_data)
print(modes)  

