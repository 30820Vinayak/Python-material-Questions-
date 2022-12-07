# Find roots of the quadratic equation
import cmath
a=int(input("Enter number1"))
b=int(input("Enter number2"))
c=int(input("Enter number3"))
d=(b*b)-(4*a*c)
s1=(-b-cmath.sqrt(d))/(2*a)
s2=(-b+cmath.sqrt(d))/(2*a)
print(s1)
print(s2)
