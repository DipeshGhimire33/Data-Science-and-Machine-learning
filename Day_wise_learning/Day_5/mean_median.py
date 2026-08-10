# To calculate mean and median for a given data

data = [1,15,32,45,8,66,74,34,66,95,15]
data.sort()
n = len(data)
mean = sum(data)/n

# median

if n % 2 !=0:
    ind = (n+1)/2
    if type(ind) == float:
        ind1=int(ind)
        ind2=int(ind)+1
        pt_val=ind-ind1
        median=data[ind1]+data[ind2]*pt_val
    else:
     median = data[ind]
else:
    median= (data[n/2]+data[(n+1)/2])/2






print(mean)
print(median)
