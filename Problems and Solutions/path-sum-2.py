# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.
# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        def find(node, total, track):
            total += node.val
            track.append(node.val)
            if node.left is None and node.right is None and total==targetSum:
                ans.append(track[:])
                return
            if node.left:
                find(node.left, total, track)
                track.pop()
            if node.right:
                find(node.right, total, track)
                track.pop()
        if root:
            find(root, 0, [])
        return ans
