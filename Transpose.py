n=int(input("enter no of rows and column"))
mat=[]
for i in range (n):
    a=[]
    for j in range(n):
        num=int(input())
        a.append(num)
    mat.append(a)
for i in range (n):
    for j in range(n):
        print(mat[j][i],end='')
    print()    
        
    