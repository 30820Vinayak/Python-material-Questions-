arr=[]
n=int(input("no of element"))
for i in range(0,n):
    a=int(input())
    arr.append(a)
for i in range(0,n-1):
    f=0
    for j in range(i+1,n):
     if (arr[i]<arr[j]):
        f=1
        break
if(f==1):
 print(arr[i])
   

    
