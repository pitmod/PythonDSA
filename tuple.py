#!/usr/bin/python3
"""Tuple"""

# Access / Traverse
print('# Access / Traverse')
tup1 = ('math', 'physics', 'bio', 4.221, 90)
tup2 = 1, 2, 5, 11
tup3 = (1,)

print('tup1:')
for i in tup1:
    print(i)
print(20*'-')

print('tup2:')
for i in tup2:
    print(i)
print(20*'-')

print('tup3:')
for i in tup3:
    print(i)
print(20*'-')



# Update
# Can't update. Can create new

tup4 = tup1 + tup2

print('tup1: ',tup1)
print('tup2: ',tup2)
print('tup4: ',tup4)

# Delete
# Can't delete elements. Can only delete all tuple

del tup1
#print(tup1)
print(20*'-')

# Length
print(len(tup2))
print(20*'-')

# Concatenation


# Repetition

print(tup2*4)
print(20*'-')


# Membership
if 11 in tup2:
    print(True)
else:
    print(False)
