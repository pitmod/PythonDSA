#!/usr/bin/python3
"""Binary tree"""

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key



r = BinaryTree('a')

print(r.getRootVal())
print(r.getLeftChild())
print(r.getRightChild())


r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())

# set d
print(r.getLeftChild().getRightChild())
r.getLeftChild().insertRight('d')
print(r.getLeftChild().getRightChild().getRootVal())

# set e and f
print(r.getRightChild().getLeftChild())
r.getRightChild().insertLeft('e')
print(r.getRightChild().getRightChild())
r.getRightChild().insertRight('f')
print(r.getRightChild().getLeftChild().getRootVal())
print(r.getRightChild().getRightChild().getRootVal())





#r.getRightChild().setRootVal('hello')
#print(r.getRightChild().getRootVal())