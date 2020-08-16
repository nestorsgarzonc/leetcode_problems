"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
"""
Result
Runtime: 68 ms, faster than 91.80% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.7 MB, less than 94.33% of Python3 online submissions for Add Two Numbers.
TODO: Refactor code :)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        valTemp=0
        actual1=l1
        actual2=l2
        temp=actual1.val+actual2.val+valTemp
        if temp>=10:
            valTemp=temp//10
            temp=temp%10
        else:
            valTemp=0
        head=ListNode(temp)
        tempHead=head
        actual1=actual1.next
        actual2=actual2.next
        while actual1 and actual2:
            temp=actual1.val+actual2.val+valTemp
            if temp>=10:
                valTemp=temp//10
                temp=temp%10
            else:
                valTemp=0
            nextNode=ListNode(temp)
            tempHead.next=nextNode
            tempHead=nextNode
            actual1=actual1.next
            actual2=actual2.next
        while actual1:
            temp=valTemp+actual1.val
            if temp>=10:
                valTemp=temp//10
                temp=temp%10
            else:
                valTemp=0
            nextNode=ListNode(temp)
            tempHead.next=nextNode
            tempHead=nextNode
            actual1=actual1.next
        while actual2:
            temp=valTemp+actual2.val
            if temp>=10:
                valTemp=temp//10
                temp=temp%10
            else:
                valTemp=0
            nextNode=ListNode(temp)
            tempHead.next=nextNode
            tempHead=nextNode
            actual2=actual2.next
        if valTemp!=0:
            nextNode=ListNode(valTemp)
            tempHead.next=nextNode
            tempHead=nextNode
        return head
            