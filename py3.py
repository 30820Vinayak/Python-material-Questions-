fo = open("myfile.txt", "r") # there is a file myfile.txt
fo.seek(10)
print ("Contents: ", fo.read())
fo.close()