# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(root):
            if not root:
                return
            
            if root.left and root.right:
                root.left,root.right = root.right,root.left
            
            elif root.left:
                root.right = root.left
                root.left = None
            else:
                root.left = root.right
                root.right = None
            
            f(root.left)
            f(root.right)
        x = root
        f(x)
        return root
