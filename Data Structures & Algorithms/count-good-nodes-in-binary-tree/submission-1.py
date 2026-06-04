# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = [0]
        def trav(node,maxi,ans):
            if not node:
                return
            if node.val >= maxi:
                ans[0]+=1
                maxi = node.val
            trav(node.left,maxi,ans)
            trav(node.right,maxi,ans)
        trav(root,float('-inf'),ans)
        return ans[0]