#Demostration Program with self
class ArithmatcOperation:
 def funAdd(self,a,b):
  self.a=a
self.b=b
add=self.a+self.b
sub=self.a-self.b
mul=self.a*self.b
div=self.a/self.b
print("addition ",add)
print("Subtraction ",sub)
print("Multiplication ",mul)
print("Division ",add)
obj=ArithmatcOperation()
obj.funAdd(40,50)
