raw_data = [["15","Ram","Kathmandu"],["10","Shyam","Biratnagar"],["20","Kiran","Jhapa"],["1","Isha","Bhaktapur"]]

sorted_data=[]
for person in range(len(raw_data)):
    sorted_data = sorted(raw_data,key = lambda x:x[0])
print(sorted_data)     
