#!/usr/bin/env python3
# Naz-Al Islam
# Dynamic Circular Buffer

# FIELDS: _block, _blockCapacity, _startIndex, _endIndex, _size

import ctypes

class CircularBuffer():
    def __init__(self, items = []):
        self._size = len(items)
        if self._size == 0:
            self._blockCapacity = 3
        else:
            self._blockCapacity = 3 * self._size
        self._block = self._makeBlock(self._blockCapacity)
        self._startIndex = self._size
        #self._endIndex = self._size - 1
        i = self._startIndex
        for item in items:
            self._block[i] = item
            i += 1
        self._endIndex = ((self._startIndex + self._size) % self._blockCapacity)

    def __len__(self):  # TESTED
        return self._size

    def __getitem__(self, index):   # TESTED
        if not 0 <= index < self._size:
            raise IndexError
        else:
            return self._block[(self._startIndex + index) % self._blockCapacity]

    def _isFull(self):
        if self._startIndex == (self._endIndex + self._blockCapacity) % 1:
            full = True
        else:
            full = False
        return full

    def _isEmpty(self):     # TESTED
        if self._startIndex == self._endIndex:
            return True
        return False

    def addToQ(self, value):
        #self._endIndex = (self._endIndex + 1) % self._blockCapacity
##        if self._isFull:
##            self._resizeBlock()
        self._block[self._endIndex] = value
        self._size += 1
        self._endIndex = (self._endIndex + 1) % self._blockCapacity

    def deleteFromQ(self):
        n = 0
##        if self._isEmpty():
##            print("Que is empty")
##        else:
        n = self._startIndex
        self._startIndex = (self._startIndex + 1) % self._blockCapacity
        self._size -= 1
        return n

##    def clearQ(self):
##        self._endIndex = -1
##        self._startIndex = self._endIndex

    def __repr__(self):
        items = []
        for i in range(0, self._size):
            items.append(self.__getitem__(i))
        return "CircularBuffer(" + repr(items) + ")"

    def _print(self):
        items = []
        for i in range(0, self._size):
            items.append(repr(self.__getitem__(i)))
            items.append(",")
        preItems = "_," * self._startIndex
        postItems = "_," * (self._blockCapacity - self._startIndex - self._size)
        print(preItems + "".join(items) + postItems,
              " capacity=", self._blockCapacity,
              " size=", self._size,
              " startIndex=", self._startIndex,
              sep = ""
            )
    def __eq__(self,  other):   # TESTED
        if self._size != other._size:
            return False
        for i in range(0, self._size):
            if self._block[self._startIndex + i] != other._block[other._startIndex + i]:
                return False
        return True



    def _makeBlock(self, capacity):
        return (capacity * ctypes.py_object)()





#=================================
##a = CircularBuffer([1,2,3])
##a._print()
###print(a.__getitem__(1))
##a.addToQ(4)
##a.addToQ(5)
##a.addToQ(6)
###a._print()
###a.addToQ(7)
##a.deleteFromQ()
##a._print()
###a.addToQ(23)
###a._print()
###a.addToQ(24)
###a._print()
###b = CircularBuffer([])
###print(b._isEmpty())
