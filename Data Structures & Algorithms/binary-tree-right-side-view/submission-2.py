# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        state = [0]
        def trav(root,state,ans):
            if root == None:
                return ans
            if len(ans) == state[0]:
                ans.append(root.val)
            state[0]+=1
            trav(root.right,state,ans)
            state[0]-=1
            state[0]+=1
            trav(root.left,state,ans)  
            state[0]-=1
            return ans   
        return trav(root,state,ans)
  
