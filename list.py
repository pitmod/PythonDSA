#!/usr/bin/python3
"""List"""

# Access / Traverse
print('# Access / Traverse')
list1 = ['math', 'physics', 'bio', 4.221, 90]
list2 = [1, 2, 5, 11]

for i in list1:
    print(i)
print(20*'-')

for i in list2:
    print(i)
print(20*'-')


print('list1[1]: ', list1[1])
print('list2[2] ', list2[2])

print(20*'-')


# Update
print('# Update')
list2[2] = 88989
for i in list2:
    print(i)
print(20*'-')


# Delete
print('# Delete')
print(list2)
del list2[0]

for i in list2:
    print(i)
print(20*'-')


# Length
print('# Length')
print(len(list1))
print(20*'-')


# Concatenation
print('# Concatenation')
print(list1+list2)
print(20*'-')

# Repetition
print('# Repetition')
print(list1*3)
print(20*'-')

# Membership
print('# Membership')
if 'hmath' in list1:
    print(True)
else:
    print(False)
print(20*'-')
print(list1)