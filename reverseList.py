# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = None
        c = head
        n = head
        
        while(c is not None):
            n = c.next
            c.next = p
            p = c
            c = n
            
        return p