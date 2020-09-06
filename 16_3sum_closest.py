"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
Accepted
"""


"""
Runtime: 292 ms, faster than 27.15% of Python3 online submissions for 3Sum Closest.
Memory Usage: 13.9 MB, less than 40.90% of Python3 online submissions for 3Sum Closest.
"""
#V 1.0
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff=float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                complement=target-nums[i]-nums[j]
                hi=bisect_right(nums, complement, j+1)
                lo=hi-1
                if hi<len(nums) and abs(complement-nums[hi])<abs(diff):
                    diff=complement-nums[hi]
                if lo>j and abs(complement-nums[lo])<abs(diff):
                    diff=complement-nums[lo]
            if diff==0:
                break
        return target-diff


#V 0.1
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        arrSum=[]
        for i in range(len(nums)-2):
            arrSum.append(nums[i]+nums[i+1]+nums[i+2])
        arrSum=sorted(arrSum)
        a=0
        b=len(arrSum)-1
        while a!=b:
            middle=b//2
            element=arrSum[middle]
            if target==element:
                return target
            elif target>element:
                a=middle
            else:
                b=middle
        return element[a]