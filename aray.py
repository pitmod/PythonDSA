#!/usr/bin/python3
"""Array"""

import array

array1 = array.array('i',[10,20,30,40,50])

# Traverse
for x in array1:
    print(x)
print(20*'-')


# Insert
array1.insert(1,60)
for x in array1:
    print(x)
print(20*'-')



# Remove
array1.remove(40)

for x in array1:
    print(x)
print(20*'-')

# Search
print(array1.index(30))
print(20*'-')

# Update
array1[2] = 100
for x in array1:
    print(x)
print(20*'-')