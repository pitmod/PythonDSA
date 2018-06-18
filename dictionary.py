#!/usr/bin/python3
"""Dictionary"""

dict1={'waza':'Ptak', 2:8, 'aaa':65.4, 3.5:(1,2,3,4,99)}
dict2={}

# Access
print('# Access')
print('dict1:', dict1)
print('dict2:', dict2)
print(20*'-')

for i in dict1:
    print(i)
print(20*'-')

print(dict1[3.5])
print(20*'-')

# Update
print('# Update')
print(20*'-')
print(dict1)
dict1['waza']='KLOC'
print(dict1)
print(20*'-')

# Delete
print('# Delete')
del dict1[3.5]
print(dict1)
del dict1
print(20*'-')


# Properties
# Key has to be unique
dict5 = {'Name': 'Zosia', 'Age': 8, 'Name':'Alicja'}
print(dict5)
print(20*'-')


# Key has to be immutable type what means it can be either a string, number ora a tuple but not list!
