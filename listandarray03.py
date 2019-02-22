'''
Traversing a list
membership
for loop
enumerate(list) functions
'''

mylist = ["apples","pears","bananas","oranges"]

# print every element of the list
# Method 1 membership

for item in mylist:
    print(item)

# Method 2 - using the index of each element



for i in range(len(mylist)):
    print(mylist[i])

# Method 3 - using enumerate()

for (ind, val) in enumerate(mylist):
    print(ind, val)