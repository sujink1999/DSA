# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        curr = 0
        q = []
        q.append((root, 0))
        arr = []
        ans = []
        while len(q) > 0:
            node, level = q.pop(0)
            if curr == level -1:
                ans.append(arr[:])
                arr = []
                curr += 1 
            for child in node.children:
                q.append((child, level+1))
            arr.append(node.val)
        ans.append(arr[:])
        return ans
