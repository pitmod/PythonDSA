#!/usr/bin/python3
"""2d array"""

T=[[1, 2, 5, 88],[32, 0, 0, 3],[8, 9, 12],[1, 9 ,99]]
print(T)

# Access / Traverse
print('# Access / Traverse')
print(T[0])
print(T[1][0])
print(20*'-')

for i in T:
    for j in i:
        print(j, end=' ')
    print()

print(20*'-')


# Update
print('# Update')
T[0] = [0, 0, 0, 0, 'dupa']
print(T)
T[1][0] = 111123
print(T)
print(20*'-')



# Delete
print('# Delete')
print(T)
del T[0]
print(T)
del T[-1][0]
print(T)

print(20*'-')
print(T)
T[-1][-1] = ['SCHABOWY','KOTLET']
print(T)
print(20*'-')
