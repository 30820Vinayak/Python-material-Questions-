f = open("data.txt", "w")
txt = "This is 1st line "
f.writelines(txt, list)
f.seek(0,0)
line = f.readlines()
print ("Read Line: %s" % (line))