raw_data = [ ["Ram","10",""],["Shyam","12","Kathmandu"],[" "," 15","Bhaktapur"],
            ["Ramkrishna","20","Kathmandu"],
            ["Shyam","","Biratnagar"],["Kiran","","Jhapa"],["Isha","","Bhaktapur"]]
    
filled_data=[]
for x in raw_data:
    name=x[0].strip()
    age=x[1].strip()
    address=x[2].strip()
    if name and age and address:
        filled_data.append(x)
    elif name and age:
        address = "Kathmandu"
        x[2]=address
        filled_data.append(x)
    elif name and address:
        age = "18"
        x[1]=age
        filled_data.append(x)
    elif age and address:
        name = "No name"
        x[0]=name
        filled_data.append(x)
print(filled_data)

sorted_data=[]
for person in range(len(filled_data)):
    sorted_data = sorted(filled_data,key = lambda x:x[1])