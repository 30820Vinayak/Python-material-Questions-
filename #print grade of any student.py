#print grade of any student
marks=int(input('enter marks'))
if (marks>85 and marks<=100):
    print("Grade A")
elif(marks>60 and marks<=85):
    print("Grade B+")
elif(marks>40 and marks<=60):
    print("Grade B")
elif(marks>30 and marks<=40):
    print("Grade c")
else:
    print("fail")


