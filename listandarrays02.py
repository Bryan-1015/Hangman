'''
Solving the assignment
'''

# Create a list of numbers
list_num = [12,15,78.3,-30,-97,12,7,-11,10]
# Order the list in ascending manner using sort()
list_num.sort()

print(list_num)
# Print the first element in the list, of index 0

print(list_num[0])
# Determine the number of the elements in the list using le(list_num)

print(len(list_num))
last_index = len(list_num)-1
print(list_num[last_index])

# Order the list in decending manner
list_num.reverse()
print(list_num)
minimum = min(list_num)
print(minimum)
maximum = max(list_num)
print(maximum)

'''
Assignment 2
'''

import random #import random #import a library to create random number
numlist = []

for i in range(20):
    numb = random.randint(-100,100)
    numlist.append(numb)
print(numlist)
numlist.sort()

print(numlist)
print("Minimum is ",numlist[0])
print()
print("Maximum is ",numlist[-1])


