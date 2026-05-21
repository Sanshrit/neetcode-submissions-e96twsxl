# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def f(node,leftval,rightval):
            if not node:
                return True
            if node.val <= leftval or node.val >= rightval:
                return False
            return f(node.left,leftval,node.val) and f(node.right,node.val,rightval)

        
        return f(root,float('-inf'),float('inf'))