"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

"""
My solution:
Runtime: 92 ms, faster than 89.33% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.1 MB, less than 44.58% of Python3 online submissions for Median of Two Sorted Arrays.
Next challenges:
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArr = sorted((nums1+nums2))
        lenArr = len(newArr)
        if lenArr % 2 == 1:
            return newArr[int(lenArr//2)]
        else:
            medium = int(lenArr//2)-1
            return (newArr[medium]+newArr[medium+1])/2
