# Implementation of Binary Search Tree 

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self.add(self.root, val)

    def remove(self, val):
        self.root = self.delete(self.root, val)

    def delete(self, node, val):
        if node is None:
            return None
        elif node.val == val:
            if node.left is None and node.right is None:
                node = None
            elif node.right is None:
                node.val = node.left.val
                node.left = self.delete(node.left, node.val)
            else:
                node.val = node.right.val
                node.right = self.delete(node.right, node.val)
            return node
        elif val > node.val:
            node.right = self.delete(node.right, val)
        else:
            node.left = self.delete(node.left, val)
        return node 
        

    def find(self, node, val):
        if node == None or node.val == val:
            return node
        if val > node.val:
            return self.find(node.right, val)
        elif val < node.val:
            return self.find(node.left, val)

    def add(self, node, val):
        if node == None:
            node = Node(val)
        elif node.val > val:
            node.left = self.add(node.left, val)
        else:
            node.right = self.add(node.right, val)
        return node

    def preorder(self):
        self.getPreorder(self.root)
        print("")

    def getPreorder(self, node):
        print(node.val, end=" ")
        if node.left:
            self.getPreorder(node.left)
        if node.right:
            self.getPreorder(node.right)





# Driver code 

bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.insert(0)
bst.insert(6)
bst.insert(7)
bst.preorder()
bst.remove(2)
bst.preorder()