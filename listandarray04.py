'''
Operation with Lists
Keywords : addition(conacatenate), slices, deleting(removing), elements
'''

import random
mylist = []

for i in range(20):
    num = random.randint(-100,100)
    mylist.append(num)
# Using traversing the list technique

suma = 0

for val in mylist:
    suma = suma + val

print(mylist)
print("The sum is :", suma)

# Using the function sum(list)

print("The sum with function sum(list)", sum(mylist))

'''
Notes
'''

alist = ["a","b","c","d","e"]
blist = ["x","y","z","w"]
print(alist + blist)

# Slices
print(alist[1 : 3])
print(alist[1 : 1])
print(alist[1 : 2])

# Squeezing technique using slices
alist[1 : 1] = blist[0 :]
print(alist)

print(alist[0 :])

