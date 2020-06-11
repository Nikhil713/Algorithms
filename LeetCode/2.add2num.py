# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result2 = result
        carry=0
        while(l1 or l2 or carry !=0):
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry,temp = divmod(val1+val2+carry,10)
            result2.next = ListNode(temp)
            result2 = result2.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return result.next