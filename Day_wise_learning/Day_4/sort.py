raw_data = [["15","Ram","Kathmandu"],["10","Shyam","Biratnagar"],
            ["20","Kiran","Jhapa"],["1","Isha","Bhaktapur"]]

# sorting based on id using sorted
sorted_data=[]
for person in range(len(raw_data)):
    sorted_data = sorted(raw_data,key = lambda x:x[0])
print(sorted_data)     

# for sorting based on address using sort
for person in range(len(raw_data)):
    raw_data.sort(key = lambda x:x[2])
print(raw_data)  


