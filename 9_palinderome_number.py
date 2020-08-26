"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
# O(log10(n))

"""
Runtime: 60 ms, faster than 81.32% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 41.89% of Python3 online submissions for Palindrome Number.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tempNum = x
        myNum = 0
        while tempNum > 0:
            myNum = myNum*10 + (tempNum % 10)
            tempNum = int(tempNum/10)
        return myNum == x


# Brute force O(n)
"""
Runtime: 112 ms, faster than 15.43% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 5.06% of Python3 online submissions for Palindrome Number.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tempNum = x
        tempN = []
        while tempNum > 0:
            tempN.append(tempNum % 10)
            tempNum = int(tempNum/10)
        myNum = 0
        for i in range(len(tempN)):
            myNum += tempN[i]*10**(len(tempN)-i-1)
        return myNum == x
