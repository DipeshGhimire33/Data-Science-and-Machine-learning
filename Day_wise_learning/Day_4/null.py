raw_data = [ ["Ram","10",""],["Shyam","12","Kathmandu"],[" "," 15","Bhaktapur"]]

clean_data=[]
for x in raw_data:
    name=x[0].strip()
    age=x[1].strip()
    address=x[2].strip()
    if name and age and address:
        clean_data.append(x)
print(clean_data)