class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

max_value = (2 ** 32) -1

class SegmentTree:
    def __init__(self, array):
        self.root = self.constructTree(0, len(array)-1, array)
        self.n = len(array)
        # self.level_order()

    def constructTree(self, left, right, array):
        if left == right:
            return Node(array[left])
        mid = (left + right) // 2
        l = self.constructTree(left, mid, array)
        r = self.constructTree(mid+1, right, array)
        node = Node(min(l.val, r.val))
        node.left = l
        node.right = r
        return node

    def query(self, left, right):
        return self.performQuery(left, right, 0, self.n -1, self.root)

    def performQuery(self, ql, qr, left, right, node):
        if ql <= left and qr >= right:
            return node.val
        if right < ql or left > qr:
            return max_value
        mid = (left + right) // 2
        return min(self.performQuery(ql, qr, left, mid, node.left), self.performQuery(ql, qr, mid+1, right, node.right))

    def level_order(self):
        stack = []
        stack.append(self.root)
        while len(stack) !=0:
            node = stack.pop(0)
            print(node.val, end=" ")
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

# Driver code
segment_tree = SegmentTree([-1, -2, 4, 0, 3, 4, 5, -10])
print(segment_tree.query(1,6))

