# Implementation of Disjoint Sets

class DisjointSets:
    def __init__(self, size):
        self.parent = [ -1 for i in range(size)]

    def find(self, x):
        if self.parent[x] != -1:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        self.parent[x_parent] = y_parent

    def print(self):
        print(self.parent)


# Driver code 
ds = DisjointSets(10)
ds.union(0,1)
ds.union(1,2)
ds.union(2,3)
ds.union(3,4)
ds.union(4,5)
ds.union(5,9)
print(ds.find(0))
ds.print()