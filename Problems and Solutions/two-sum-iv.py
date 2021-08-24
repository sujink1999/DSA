# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return false
        s = set()
        def find(node):
            if (k - node.val) in s:
                return True
            s.add(node.val)
            if node.left:
                if find(node.left):
                    return True
            if node.right:
                if find(node.right):
                    return True
            return False
        return find(root)
