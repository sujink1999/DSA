# You are given a string s of lowercase English letters and an integer array shifts of the same length.
# Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
# Return the final string after all such shifts to s are applied.

# Example 1:

# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        aton = dict(zip([i for i in "abcdefghijklmnopqrstuvwxyz"], range(26)))
        ntoa = dict(zip(range(26), [i for i in "abcdefghijklmnopqrstuvwxyz"]))
        s = list(s)
        total = 0
        for i in range(len(s)-1,-1,-1):
            total = (shifts[i] + total) % 26
            val = (aton[s[i]] + total) % 26
            s[i] = ntoa[val]
        return "".join(s)
