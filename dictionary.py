def sumoflist(l):
  total = 0
  for val in l:
    total = total + val
  return total

my_list = [8,2,3,0,7]
print ("The sum of my_list is", sumoflist(my_list))