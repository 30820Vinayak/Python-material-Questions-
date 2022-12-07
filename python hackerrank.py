arr=[]
n=int(input('enter element'))
for i in range(0,n):
   a=int(input(''))
   arr.append(a)
for i in range(1,n):
   if(arr[i]>=arr[i-1]):
        temp=arr[i-1]
        arr[i-1]=arr[i]
        arr[i]=temp
   if(arr[i]<=arr[i-1]):
        temp=arr[i-1]
        arr[i-1]=arr[i]
        arr[i]=temp
print(arr)



