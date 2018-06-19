#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self,item):
        self.items.pop(item)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s=Stack()
s.push('sth')
s.push('dsafdsfds')
s.push(9)
s.push(9.88)





