a = ["Ramesh","Suresh","Dipesh"]
for i, v in enumerate(a):
    print(i, v)

b ={'Ramesh': 115,'Suresh': 136,'Dipesh': 603}
print(b)

print(list(enumerate(b.items())))               # list presents in list view, items() is used to return key value pair