# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        state = [0]
        ans = [0]
        def trav(node,state):
            if node:
                trav(node.left,state)
                state[0]+=1
                if state[0] == k:
                    ans[0] = node.val
                    return
                trav(node.right,state)
            return
        trav(root,state)
        return ans[0]


        