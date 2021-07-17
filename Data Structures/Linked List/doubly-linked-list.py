# Implementation of Doubly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

head = Node(1)
curr = head
for i in range(2,11):
    temp = Node(i)
    temp.prev = curr
    curr.next = temp
    curr = curr.next

while(head):
    print("Node is ",head.val,end=".")
    if head.prev:
        print(" prev is ",head.prev.val, end=".")
    if head.next:
        print(" next is ",head.next.val, end=".")
    print("\n")
    head = head.next