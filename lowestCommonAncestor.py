# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #self.printTree(root)
        
        if(root == None):
            return None
        if(root == p or root == q):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left == None and right == None:
            return None
        if left == None:
            return right
        if right == None:
            return left
         
        if left == p and right == q:
            return root
        if left == q and right == p:
            return root
        
    def printTree(self, root):
        if root == None:
            return
        
        self.printTree(root.left)
        print root
        self.printTree(root.right)
        
        return
        

        