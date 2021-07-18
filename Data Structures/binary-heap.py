# Implementation of Binary Heap ( min heap )

class Heap:
    def __init__(self):
        self.arr = []

    def add(self, val):
        self.arr.append(val)
        self.swim(len(self.arr) -1)
    
    def remove(self):
        val = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.sink(0)
        return val

    def sink(self, index):
        left = index*2 + 1
        right = index*2 + 2
        next = self.lesser(right, left)

        while next is not None and self.arr[index] > self.arr[next]:
            self.arr[next], self.arr[index] = self.arr[index], self.arr[next]
            index = next
            left = index*2 + 1
            right = index*2 + 2
            next = self.lesser(right, left)

    def swim(self, index):
        parent = (index-1) // 2
        while index>0 and self.arr[index] < self.arr[parent]:
            self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            index = parent
            parent = (index-1) // 2


    def lesser(self, right, left):
        if left >= len(self.arr):
            return None
        elif right >= len(self.arr):
            return left
        else:
            return right if self.arr[right] < self.arr[left] else left


# Driver function

heap = Heap()

for i in range(10, 0, -1):
    heap.add(i)

print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())
heap.add(2)
print(heap.remove())


