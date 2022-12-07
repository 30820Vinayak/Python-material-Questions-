n=int(input("Enter a number"))
sum=0
for i in range (1,n):
    if (n%i==0):
        sum=sum+i
    if (sum==n):
       print("it is a a strong number")
    else:
        print("it is not a strong number")