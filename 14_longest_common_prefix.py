

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

"""
Runtime: 40 ms, faster than 51.41% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 80.44% of Python3 online submissions for Longest Common Prefix.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        if strs[0] == '':
            return ''
        firstLetterArray = list(strs[0])
        isTrue = True
        myString = ''
        try:
            for index in range(len(firstLetterArray)):
                for srt in strs:
                    if srt[index] != firstLetterArray[index]:
                        isTrue = False
                if isTrue:
                    myString += firstLetterArray[index]
                else:
                    return myString
        except:
            return myString
        return myString
