# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []


def threeSum(a):
    a.sort()
    ans = set()
    for i in range(len(a)-2):
        j = i+1
        k = len(a)-1
        while j < k:
            total = a[i] + a[j] + a[k]
            if total > 0:
                k-=1
            elif total < 0:
                j+=1
            else:
                ans.add((a[i], a[j], a[k]))
                j+=1
    return list(ans)