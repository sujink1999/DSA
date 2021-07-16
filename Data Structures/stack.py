# Implementation of Stack

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def peek(self):
        if len(self.arr)>0:
            return self.arr[-1]
        return None

    def pop(self):
        return self.arr.pop()

    def print(self):
        print(self.arr)

stack = Stack()
stack.print()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()
print('PEEK VALUE IS ',stack.peek())
stack.pop()
stack.pop()
print("STACK AFTER POP")
stack.print()

