# create a program to compare lists and output the common numbers
# generate random lists to compare
import random


a = []
for i in range(0, 6):
    n = random.randint(0, 10)
    a.append(n)

b = [2, 3, 5, 6, 8, 10]

#for element in a:
 #   if element in b:
  #      print(element)
c = []
[c.append(x) for x in a if x in b if x not in c]
print(c)
