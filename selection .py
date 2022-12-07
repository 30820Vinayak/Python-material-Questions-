def selection(arr,length):
    for i in range(0,length-1):
        min=i
        for j in range(i+1,length):
            if(arr[j]<arr[min]):
                min=j
        (arr[min],arr[i])=(arr[i],arr[min])
arr=[10,5,8,2,19,7]
length=len(arr)
selection(arr,length)
print(arr)


