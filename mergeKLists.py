# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        p = PriorityQueue()
        for node in lists:
            if node is not None:
                p.put((node.val, node))
        prev = None      
        while not p.empty():
            val, temp = p.get()
            tempN = temp.next
            if(tempN is not None):
                p.put((tempN.val, tempN))
            if(prev is None):
                head = temp
                prev = temp
            else:
                prev.next = temp
                prev = temp
                
        return head