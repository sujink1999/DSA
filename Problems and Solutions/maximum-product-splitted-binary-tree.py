# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
# Note that you need to maximize the answer before taking the mod and not after taking it.

# Example 1:

# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        def find(node):
            total = node.val
            if node.left:
                total += find(node.left)
            if node.right:
                total += find(node.right)
            sums.append(total)
            return total
        find(root)
        ans = 0
        for i in range(len(sums)-1):
            ans = max(ans, (sums[-1] - sums[i])* sums[i])
        return ans % (10**9 + 7)
