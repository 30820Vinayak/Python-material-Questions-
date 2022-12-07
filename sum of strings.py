def find_ten_substring(num_str):
    m=[]
    l=[]
    for i in range(0,len(num_str)):
        s=0
        for j in range(i,len(num_str)):
            m.append(num_str[i:j+1])  
            s=s+int(num_str[j])
            if(s==10 and b+1==len(k)):
                l.append(num_str[i:j+1])     
    return l
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)