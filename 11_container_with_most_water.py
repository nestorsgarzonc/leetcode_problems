
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Image link: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

"""
Runtime: 124 ms, faster than 93.68% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.3 MB, less than 87.15% of Python3 online submissions for Container With Most Water.
"""
#Best solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        leftPoint=0
        rightPoint=len(height)-1
        while leftPoint!=rightPoint:
            maxArea=max(maxArea, (rightPoint-leftPoint)*min(height[leftPoint],height[rightPoint]))
            if height[leftPoint]>height[rightPoint]:
                rightPoint-=1
            else:
                leftPoint+=1
        return maxArea