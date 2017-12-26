# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1, len2 = 0, 0
        
        temp = headA
        while temp is not None:
            temp = temp.next
            len1 += 1
            
        temp = headB
        while temp is not None:
            temp = temp.next
            len2 += 1
            
        if(len1 == 0 or len2 == 0):
            return None
        
        p1 = headA
        p2 = headB
        if len1>len2:
            dif = len1-len2
            while dif>0 and p1.next is not None:
                p1 = p1.next
                dif -= 1
            if dif != 0:
                return None
                
                
        elif len2>len1:
            dif = len2-len1
            while dif>0 and p2.next is not None:
                p2 = p2.next
                dif -= 1
            if dif != 0:
                return None
                
        while(p1 != p2 and p1 is not None and p2 is not None):
            p1 = p1.next
            p2 = p2.next
            
        if(p1 != p2):
            return None
            
        return p1
