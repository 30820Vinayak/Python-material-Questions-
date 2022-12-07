furniture={"sofa":1000000,"dining":3000000}
choice="YES"
sum=0
while(choice!="No"):
    b=input("enter what more you want")
    a=int(input("enter quantity"))
    sum=sum+a*(furniture.get(b))
    choice=input('do you want to continue')
print(sum)
