def ap(arr):
    arr.sort();
    d=(arr[1]-arr[0])
    for i in range(len(arr)):
         if(arr[i]-arr[i+1]!=d):
             return False
         else:
            return True
arr=[4,6,8,10.12]
ap(arr)
        

