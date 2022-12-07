
def sum(*args):
    resultfinal = 0

    for arg in args:
        resultfinal = resultfinal + arg

    return resultfinal

print(sum(10, 20))            #
print(sum(10, 20, 30))        
print(sum(10, 20, 2))        