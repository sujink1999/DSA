# Implementation of queue

class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, val):
        self.arr.append(val)

    def front(self):
        if len(self.arr)>0:
            return self.arr[0]
        return None

    def rear(self):
        if len(self.arr)>0:
            return self.arr[-1]
        return None

    def dequeue(self):
        return self.arr.pop(0)

    def print(self):
        print(self.arr)

queue = Queue()
queue.print()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.print()
print('FRONT VALUE IS ',queue.front())
print('REAR VALUE IS ',queue.rear())
queue.dequeue()
queue.dequeue()
print("QUEUE AFTER DEQUEUE")
queue.print()