#!/usr/bin/python3
"""Node"""

class DayNames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = DayNames('Mon')
e2 = DayNames('Tue')
e3 = DayNames('Wed')
e4 = DayNames('Thu')



e1.nextval = e2
e2.nextval = e3
e3.nextval = e4

thisvalue = e1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval



