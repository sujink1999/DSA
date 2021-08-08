# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# Example 1:

# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution:
    def minCut(self, s: str) -> int:
        d = {}
        def isPalindrome(i,j):
            return s[i:j+1]==s[i:j+1][::-1]
        def find(i):
            if i < 0:
                return -1
            elif i == 0:
                return 0
            if i in d:
                return d[i]
            ans = 2**32 -1
            for j in range(i+1):
                if isPalindrome(j,i):
                    ans = min(ans, find(j-1)+1)
            d[i] = ans
            return ans
        return find(len(s)-1)
