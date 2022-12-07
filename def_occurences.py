def_occurences(arr)
count=0
n=len(arr)
for i in range(0,n-1):
    if(arr[i]==arr[i+1]):
        count+=1 
return count
list=[1,1,1,2,2,2,2,2,]
b=occurences(list)
print(b)

