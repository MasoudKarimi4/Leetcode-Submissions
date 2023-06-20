# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        list = []
        
        
        def trav(root):
            
            if not root:
                return
            
            trav(root.left)
            trav(root.right)
            
            list.append(root.val)
        
        trav(root)
        
        return list 
        