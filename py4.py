f = open("testfile", "r")
 f.write("This is the test file for exception handling!!")
except IOError:
   print ("Error: could not find a file or read data")
finally:
   print ("In finally part")
else:
   print ("content is written in the file successfully")