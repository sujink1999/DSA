# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.

# Example 1:

# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        if len(s) == 0:
            return 0
        count = 0
        arr = []
        for i in s:
            if i == "1":
                count+=1
            arr.append(count)        
        n = len(s)
        zeros = n-arr[-1]
        ans = zeros
        for i in range(n):
            left_ones = arr[i]
            right_ones = arr[n-1]-left_ones
            right_zeros = n-i-1 - right_ones
            ans = min(left_ones+right_zeros, ans)
        return ans
