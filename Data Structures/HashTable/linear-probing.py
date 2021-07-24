# Implementation of Hashtable Linear Probing

class Hashtable:
    def __init__(self, n):
        self.arr = [''] * n
        self.length = n

    def hash(self, x):
        return x % self.length

    def insert(self, val):
        index = self.hash(val)
        count = 0
        while self.arr[index] != "" and count < self.length:
            index = (index+1)%self.length
            count+=1
        if count == self.length:
            print("Hashtable is full")
        else:
            self.arr[index] = val

    def search(self, val):
        index = self.hash(val)
        count = 0
        while self.arr[index] != "" and self.arr[index]!=val and count < self.length:
            index = (index+1)%self.length
            count+=1
        if count == self.length or self.arr[index] == "":
            print("Not present")
        else:
            print("Found at index ",index)

# Driver code
hashtable = Hashtable(5)
hashtable.insert(5454)
hashtable.insert(87554)
hashtable.insert(84872)
hashtable.insert(24515)
hashtable.insert(185456)
hashtable.insert(45156)
hashtable.search(7824)
hashtable.search(87554)

