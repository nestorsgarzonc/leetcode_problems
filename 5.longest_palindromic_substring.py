"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


#Brute force solution O(n**2)
"""
Runtime: 7420 ms, faster than 10.35% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14 MB, less than 34.65% of Python3 online submissions for Longest Palindromic Substring.
"""

class Solution:
    def longestPalindrome(self, s: str) -> çstr:
        if s==s[::-1]:
            return s
        lonSub=''
        for i in range(0, len(s)):
            for window in range(len(s)-i):
                subS=s[i: len(s)-window]
                if subS==subS[::-1]:
                    if len(subS)>len(lonSub):
                        lonSub=subS
        return lonSub