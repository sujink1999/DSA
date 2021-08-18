# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def find(node, max_so_far):
            nonlocal ans
            if node.val >= max_so_far:
                ans += 1
            max_so_far = max(max_so_far, node.val)
            if node.left:
                find(node.left, max_so_far)
            if node.right:
                find(node.right, max_so_far)
        find(root, -2**32)
        return ans
