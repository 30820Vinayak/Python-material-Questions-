def gcd(x,y):
    if(x==0):
        return y
    else:
        return gcd(y%x,x)
x=int(input("enter the first no."))
y=int(input("enter the second n0."))
hij=gcd(x,y)
print(hij)