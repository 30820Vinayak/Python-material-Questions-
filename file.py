file=open("file.txt","r")
f=0
fw=""
a=[]
for i in file: 
    a=line.upper().replace(',','').replace('.','').split(" ")
    for j in a:
        a.append(j)
for k in range(0,len(a)):
    c=0
    for g in range(k+1,len(a)):
        if(a[i]==a[j]):
            c=c+1
            
    if(c>f):
        f=c
        fw=w[i]

print("word=",+fw)
print("Frequncy",str(f))
file.close()