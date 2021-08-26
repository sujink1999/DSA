# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = set()
        for i in range(int(c**0.5)+1):
            val = i ** 2
            s.add(val)
            if c - val in s:
                return True
        return False
