# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        if root is None:
            return []
        
        q.append(root)
        while q:
            temp = []*len(q)
            k = len(q)
            for i in range(k):
                x = q.popleft()
                temp.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            ans.append(temp)
        return ans
        