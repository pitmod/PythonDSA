#!/usr/bin/python3
"""Set"""

# Access
# We can't access individual values in a set!


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
Sth=set()
print(Days)
print(Months)
print(Dates)
print(20*'-')

for i in Days:
    print(i)
print(20*'-')

# Add items to a set
print('# Add items to a set')
Days.add('KUPSZTAL')
print(Days)
print(20*'-')



# Remove items from set
print('# Remove items from a set')
Days.discard('KUPSZTAL')
print(Days)

print(20*'-')

## Set operations
print('## Set operations')

print(20*'#')
print(20*'#')
print(20*'#')

DaysA=set(["Mon","Tue","Wed"])
DaysB=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

print('DaysA:')
print(DaysA)
print(20*'#')

print('DaysB:')
print(DaysB)
print(20*'#')


# Union
print('# Union')
MyDays = DaysA | DaysB
print(MyDays)
print(20*'#')

# Intersection
print('# Intersection')
MyDays = DaysA & DaysB
print(MyDays)
print(20*'#')

# Difference
print('# Difference A-B')
MyDays = DaysA - DaysB
print(MyDays)
print(20*'#')

# Difference
print('# Difference B-A')
MyDays = DaysB - DaysA
print(MyDays)
print(20*'#')


# Symetric difference
print('# Symetric difference A^B')
MyDays = DaysA ^ DaysB
print(MyDays)
print(20*'#')


# Subset/Superset
print('# Subset/Superset')
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA

print('SubsetRes = DaysA <= DaysB :', SubsetRes)
print('SupersetRes = DaysB >= DaysB :', SupersetRes)



print(20*'#')



