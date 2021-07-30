# Implementation of Segment tree using arrays

import math

max_value = (2 ** 32) -1

class SegmentTree:
    def __init__(self, array):
        next_power_of_2 = int(math.ceil(math.log2(len(array))))
        max_size = 2 * ( 2 ** next_power_of_2) -1
        self.tree = [0] * max_size
        self.constructTree(0, len(array)-1, 0, array)
        print(self.tree)

    def constructTree(self, left, right, parent, array):
        if left == right:
            self.tree[parent] = array[left]
            return 
        mid = (left + right) // 2
        self.constructTree(left, mid, 2*parent+1, array)
        self.constructTree(mid+1, right, 2*parent+2, array)
        self.tree[parent] = min(self.tree[2*parent+1], self.tree[2*parent+2])

    def query(self, ql, qr, left, right, pos):
        if ql <= left and qr >= right:
            return self.tree[pos]
        if right < ql or left > qr:
            return max_value
        mid = (left + right) // 2
        return min(self.query(ql, qr, left, mid, 2*pos+1), self.query(ql, qr, mid+1, right, 2*pos+2))

# Driver code
segment_tree = SegmentTree([-1, -2, 4, 0, 3, 4, 5, -10])
print(segment_tree.query(1,7,0,7,0))
