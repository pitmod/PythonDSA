#!/usr/bin/python3
"""Singly Linked List"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head=None

    def listprint(self):
        value = self.head
        while value:
            print(value.data)
            value = value.next

    def addbeg(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def addend(self,data):
        value = self.head
        newnode = Node(data)
        if value == None:
            self.head = newnode
            return
        while value.next:
            value = value.next
        value.next = newnode

    def size(self):
        value = self.head
        counter = 0
        while value:
            counter += 1
            value = value.next
        return counter

    def search(self,data):
        value = self.head
        searchval = data
        while value:
            if value.data == searchval:
                return True
            value = value.next
        return False

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next



d1 = Node("Mon")
d2 = Node("Tue")
d3 = Node("Wed")

d1.next = d2
d2.next = d3

list1 = SLinkedList()
list1.head = d1

list1.listprint()
print(20*'#')


list1.addbeg("Sun")
list1.listprint()
print(20*'#')

list1.addend("Thu")
list1.listprint()
print(20*'#')

print(list1.size())
print(20*'#')

print(list1.search("Mon"))
print(20*'#')

list1.remove("Thu")
list1.listprint()
print(20*'#')
