# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr = []
        d = {}
        ans = []
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                arr.append(i)
                d[i]=1
        def find(i, a):
            if i == len(arr):
                ans.append(a[:])
                return
            find(i+1, a)
            for j in range(d[arr[i]]):
                find(i+1, [arr[i]] * (j+1) + a )
        find(0,[])
        return ans
