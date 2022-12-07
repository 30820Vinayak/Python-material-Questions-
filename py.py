f = None
for i in range(5):
    if i > 2:
        break
 
with open("data.txt", "r") as f:
    print(f.read())
 
    f.close()