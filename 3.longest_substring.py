"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

""""
Runtime: 44 ms, faster than 98.89% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.7 MB, less than 95.60% of Python3 online submissions for Longest Substring Without Repeating Characters.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempString = ''
        maxSequence = 0
        for i in range(len(s)):
            if s[i] not in tempString:
                tempString += s[i]
                maxSequence = max(maxSequence, len(tempString))
            else:
                y = tempString.index(s[i])
                tempString = tempString[y+1:]
                tempString += s[i]
        return m
