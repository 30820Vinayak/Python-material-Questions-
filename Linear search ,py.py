def linear_Search(list1, n, val):  
 for i in range(0, n):  
        if (list1[i] == val):  
            return i   
list1 =[5,4,8,9,10,14]  
val = 9 
  
n = len(list1)  
res = linear_Search(list1, n, val)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res) 