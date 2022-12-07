#Largest of three numbers
num1=float(input('enter number 1:'))
num2=float(input('enter number 2:'))
num3=float(input('enter number 3:'))
if (num1>num2 and num1>num3):
    print("num 1 is largest")
elif (num2>num1 and num2>num3):
    print("num 2 is largest")
else:
    print("num 3 is largest")

