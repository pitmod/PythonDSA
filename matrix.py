#!/usr/bin/python3
"""Matrix"""
from numpy import *
a = array([['Mon',1822,20,22,17],
                ['Tue', 11, 18, 21, 18],
                ['Wed', 15, 21, 20, 19],
                ['Thu', 11, 20, 22, 21]
                ])

m = reshape(a,(4,5))
print(m)

# Access
print('# Access')
print(m[0])
print(m[1][1])

# Add row at the end (0 defines an axis x so row)
m_r = append(m,[['Avg',12,15,22,22]],0)
print(m_r)
print(20*'-')

#m_z = append(m,[['A'],['B'],['C'],['D']],1)
m_z = append(m,[['A','B','C','D']],1)
print(m_z)
print(20*'-')


# Add column
m_c = insert(m,[1],[[1],[2],[3],[4]],1)
print(m_c)
print(20*'-')


