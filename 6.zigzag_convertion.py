"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


"""
1158 / 1158 test cases passed.
Status: Accepted
Runtime: 88 ms
Memory Usage: 13.9 MB

"""
# Solution brute force


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arrResult = [[] for i in range(numRows)]
        counter = 0
        numRows -= 1
        reverse = False
        for i in s:
            if counter == numRows:
                reverse = True
            if counter == 0:
                reverse = False
            if counter < numRows and reverse == False:
                arrResult[counter].append(i)
                counter += 1
            if counter > 0 and reverse == True:
                arrResult[counter].append(i)
                counter -= 1

        myResult = ''
        for i in arrResult:
            myResult.join(i)
        return myResult
