n={}
a=int(input("Enter size of dictionary"))
list=[]
for i in range(a):
    b=int(input())
    n[i]=b
print("dictionary",n)
for i in range(a):
    if(n[i]%2==0):
        list.append(n[i])
print("Even number in dictionary",list)
