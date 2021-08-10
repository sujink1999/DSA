# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
# You must also not convert the inputs to integers directly.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        it =0
        c= 0
        ans = ''
        while it < len(num1) and it < len(num2):
            a = int(num1[it])
            b = int(num2[it])
            ans += str((a+b+c)%10)
            c = (a + b + c) // 10
            it+=1
            
        while it < len(num1):
            a = int(num1[it])
            ans += str((a+c)%10)
            c = (a + c) // 10
            it+=1
            
        while it < len(num2):
            a = int(num2[it])
            ans += str((a+c)%10)
            c = (a + c) // 10
            it+=1
            
        if c > 0:
            ans += str(c)
            
        return ans[::-1]
