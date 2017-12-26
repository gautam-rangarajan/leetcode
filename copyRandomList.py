# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        
        randP = dict()
        oldToNew = dict()
        temp = head
        while temp is not None:
            print temp.label
            temp = temp.next

        
        while temp is not None:
            randP[temp] = temp.random
            node = self.copyNode(temp)
            oldToNew[temp] = node
            temp = temp.next
        
        for oldNode, oldRand in randP.items():
            #print oldNode.label
            newNode = oldToNew[oldNode]
            oldNext = oldNode.next
            #print oldNext.label
            newNext = oldNode[oldNext]
            if oldRand in oldToNew.keys():
                newRand = oldToNew[oldRand]
            else:
                newRand = oldRand
            newNode.next = newNext
            newNode.random = newRand
        
        return oldToNew[head]
    
    def copyNode(self, node):
        newNode = RandomListNode(node.label)
        newNode.random = node.random
        newNode.next = node.next
        return newNode
        