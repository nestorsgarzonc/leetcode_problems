"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows."""

"""
Runtime: 40 ms, faster than 38.79% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.7 MB, less than 84.66% of Python3 online submissions for Reverse Integer.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x*-1
            num = str(x)[::-1]
            result = int(num)*-1
        else:
            num = str(x)[::-1]
            result = int(num)
        if result > 2147483647 or result < -2147483647:
            return 0
        else:
            return result
