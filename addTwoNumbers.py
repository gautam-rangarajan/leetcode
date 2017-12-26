# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        temp1 = l1
        temp2 = l2
        prevNode = None
        quot = 0
        while(temp1 != None or temp2 != None or quot != 0):
            if(temp1 != None):
                val1 = temp1.val
            else:
                val1 = 0 
 
            if(temp2 != None):
                val2 = temp2.val
            else:
                val2 = 0
            
            tot = val1+val2+quot
            rem = tot%10
            curNode = ListNode(rem)
            quot = tot/10
            
            if(prevNode is not None):
                prevNode.next = curNode
                prevNode = curNode
            else:
                head = curNode
                prevNode = curNode
            
            if(temp1 is not None):
                temp1 = temp1.next
            
            if(temp2 is not None):
                temp2 = temp2.next
            
        return head
        
    def printList(self, curNode):
        head = curNode
        while(head != None):
            print head.val,
            head = head.next
        print ""