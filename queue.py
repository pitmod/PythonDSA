#!/usr/bin/python3
"""Queue"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(3)
q.enqueue(44.66)
q.enqueue('jan')
q.enqueue([1,2,3])
print(q.size())
print(q.items)
q.dequeue()
print(q.size())
print(q.items)





