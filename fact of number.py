def fact_ofanumber(f):
    fact=1
    for i in range(1,f+1):
        fact*=i
    return fact
        
print(fact_ofanumber(5))