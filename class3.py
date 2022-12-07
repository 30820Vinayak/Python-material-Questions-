class SelfDemoProgram:
 def __init__(self,name,age):
    self.name=name
self.age=age
def display(self):
    print(self.name)
    print(self.age)
name=input("enter name")
age=int(input("enter Age"))
obj=SelfDemoProgram(name,age)
obj.display()
