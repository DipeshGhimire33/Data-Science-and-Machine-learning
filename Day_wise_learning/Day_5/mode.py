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

# without any libraries

data =[1,1,2,2,3,3,3,4,5,5]
count_dic ={}
data.sort()

for i in data:
    count=0
    for j in range(len(data)):
        if i == data[j]:
            count= count +1
    count_dic[i]=count
print(count_dic) 

freq=[]
for num in count_dic:
    freq.append(count_dic[num])
    freq.sort(reverse=True)
    mode = next(k for k,v in count_dic.items() if v==freq[0])
print(mode)

