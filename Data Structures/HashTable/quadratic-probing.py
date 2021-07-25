# Implementation of Hashtable Quadratic Probing

class Hashtable:
    def __init__(self, n):
        self.arr = [''] * n
        self.length = n

    def hash(self, x):
        return x % self.length

    def insert(self, val):
        index = self.hash(val)
        for i in range(1,self.length):
            n_index = (index + (i*i) )%self.length
            if self.arr[n_index] == "":
                self.arr[n_index] = val
                break

    def search(self, val):
        index = self.hash(val)
        for i in range(1,self.length):
            n_index = (index + (i*i) )%self.length
            if self.arr[n_index] == val:
                print("Found at index ",n_index)
                break

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