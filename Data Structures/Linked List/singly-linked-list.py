# Implementation of Single Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = Node(1)
curr = head
for i in range(2,11):
    temp = Node(i)
    curr.next = temp
    curr = curr.next

while(head):
    print("Node is ",head.val,", next is ",head.next)
    head = head.next