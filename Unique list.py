def uniquelist(u):
    x=[]
    for a in u:
        if a not in x:
            x.append(a)
    return x
print(uniquelist([1,2,2,3,3,4,4,5,5]))
