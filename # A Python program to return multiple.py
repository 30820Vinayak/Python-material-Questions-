# A Python program to return multiple
# values from a method using class
class Test:
	 def _init_(self):
		 self.str = "hello world"
		t5self.x = 20

# This function returns an object of Test
def fun():
	return Test()
	
# Driver code to test above method
t = fun()
print(t.str)
print(t.x)