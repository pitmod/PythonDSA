#!/usr/bin/python3
"""Node"""

class DayNames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

d1 = DayNames('Mon')
d2 = DayNames('Tue')
d3 = DayNames('Wed')

d1.nextval = d2
d2.nextval = d3


thisval = d1

while thisval:
    print(thisval.dataval)
    thisval = thisval.nextval
