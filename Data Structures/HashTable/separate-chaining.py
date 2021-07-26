# Implementation of Hashtable Linear Probing

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Hashtable:
    def __init__(self, n):
        self.arr = [None] * n
        self.length = n

    def hash(self, x):
        return x % self.length

    def insert(self, val):
        index = self.hash(val)
        if not self.arr[index]:
            self.arr[index] = Node(val)
        curr = self.arr[index]
        while curr.next != None:
            curr = curr.next
        curr.next = Node(val)

    def search(self, val):
        index = self.hash(val)
        curr = self.arr[index]
        while curr != None:
            if curr.val == val:
                print("Found at index ",index)
                break
            curr = curr.next

# Driver code
hashtable = Hashtable(5)
hashtable.insert(5454)
hashtable.insert(87554)
hashtable.insert(84872)
hashtable.insert(24515)
hashtable.insert(185456)
hashtable.insert(45156)
hashtable.search(45156)
hashtable.search(87554)
