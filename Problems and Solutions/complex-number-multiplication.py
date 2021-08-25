# A complex number can be represented as a string on the form "real+imaginaryi" where:
# real is the real part and is an integer in the range [-100, 100].
# imaginary is the imaginary part and is an integer in the range [-100, 100].
# i2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.
# Example 1:
# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def separate(x):
            arr = x.split('+')
            return [int(arr[0]), int(arr[1][:-1])]
        a = separate(num1)
        b = separate(num2)
        return str(a[0]*b[0] - (a[1]* b[1]))+'+'+str((a[0]*b[1]) + (a[1]* b[0]))+'i'
