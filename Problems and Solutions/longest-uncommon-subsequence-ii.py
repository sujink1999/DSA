# Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc".
# Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

# Example 1:
# Input: strs = ["aba","cdc","eae"]
# Output: 3

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s, sub):
            i = 0
            j = 0
            while(i<len(s) and j<len(sub)  and (len(s)-i) >= (len(sub)-j)):
                if s[i] == sub[j]:
                    j+=1
                i+=1
            return j==len(sub)
        strs.sort(key = lambda x: len(x), reverse=True)
        for i, sub in enumerate(strs):
            flag = True
            for j in range(len(strs)):
                if i!=j and isSubsequence(strs[j], sub):
                    flag = False
            if flag:
                return len(sub)
        return -1
