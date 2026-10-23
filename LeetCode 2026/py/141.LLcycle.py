# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowNode = head
        fastNode = head

        while fastNode and fastNode.next != None:
            slowNode = slowNode.next
            fastNode = fastNode.next.next 
            if slowNode == fastNode:
                return True
            
        return False