# list within a list

list1=[1,2,3,4,5,6,7,8,9,0]

list2=[[1,2],[3,4],[5,6],[7,8],[9,0]]

for i in list1:
    print(i)

for i in list2:
    print(i)

for i in list2:
    for j in i:
        print(j)

print(list2[0][1])