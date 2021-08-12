# Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, 
# or false otherwise.

# Example 1:

# Input: arr = [3,1,3,6]
# Output: false

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d = {}
        pos = []
        neg = []
        def remove(val):
            if d[val] == 1:
                del d[val]
            else:
                d[val] -= 1
        for i in arr:
            pos.append(i) if i > 0 else neg.append(i)
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        pos.sort()
        neg.sort()
        for i in pos + neg[::-1]:
            if i in d:
                remove(i)
                if 2*i in d:
                    remove(2*i)
                else:
                    return False
        return len(d)==0
