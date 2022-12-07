java_course = {"John", "Jack", "Jill", "Joe"}
Python_course = {"Jake", "John", "Eric", "Jill"}

print("Students enrolled in Python course:", len(Python_course))
print("\n")
print("Students enrolled in Java course: ")
for i in java_course:
    print(i)
print("\n")
print("Students enrolled in Python course: ")
for j in Python_course:
    print(j)
print("\n")
print("Students enrolled for both courses:",java_course.intersection(Python_course))
not_both = java_course.difference(Python_course) | Python_course.difference(java_course)
len_not_both = len(not_both)
print("Students enrolled for either one not for both:\n","Total:",len_not_both,"Names:", not_both)
print("\n")
print("Students enrolled either one course:\n","Total:", len(java_course.union(Python_course)), "Names:", java_course.union(Python_course))