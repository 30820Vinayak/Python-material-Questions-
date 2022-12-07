s=str(input("enter string"))
upper=0
lower=0
for i in s:
  if(i.isupper()):
    upper+=1 
  elif(i.islower()):
    lower+=1
print(upper)
print(lower)
