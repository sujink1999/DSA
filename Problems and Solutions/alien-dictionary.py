# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, 
# return true if and only if the given words are sorted lexicographicaly in this alien language.

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        for i in range(1,len(words)):
            ind = 0
            while ind < len(words[i]) and ind < len(words[i-1]):
                if d[words[i][ind]] < d[words[i-1][ind]]:
                    return False
                elif d[words[i][ind]] > d[words[i-1][ind]]:
                    break
                ind+=1
            if ind == len(words[i]) and ind < len(words[i-1]):
                return False
        return True
