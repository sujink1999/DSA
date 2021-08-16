# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, 
# return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        d1 = Counter(t)
        length = len(d1)
        
        d2 = {}
        left = 0
        right = 0
        formed = 0
        if s[left] in d1:
            d2[s[left]] = 1
            if d2[s[left]] == d1[s[left]]:
                formed += 1
        ans = None
        while left <= right:
            if formed == length:
                if ans:
                    ans = s[left:right+1] if len(ans) > right+1-left else ans
                else:
                    ans = s[left:right+1]
                if s[left] in d1:
                    d2[s[left]] -= 1
                    if d2[s[left]] < d1[s[left]]:
                        formed -= 1
                left += 1
            else:
                right += 1
                if right == len(s):
                    break
                if s[right] in d1:
                    if s[right] in d2:
                        d2[s[right]] += 1
                    else:
                        d2[s[right]] = 1
                    if d2[s[right]] == d1[s[right]]:
                        formed += 1
                
        return ans if ans != None else ""
