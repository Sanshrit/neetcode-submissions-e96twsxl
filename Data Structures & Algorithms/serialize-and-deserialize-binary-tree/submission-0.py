# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        if not root:
            return ""
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node is None:
                s.append('#,')
            else:
                s.append(str(node.val) + ',')
                q.append(node.left)
                q.append(node.right)
        s = "".join(ch for ch in s)
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        vals = data.split(",")
        vals.pop()
        root = TreeNode(int(vals[0]))
        idx=1
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()

            #left
            if vals[idx]!='#':
                node.left = TreeNode(int(vals[idx]))
                q.append(node.left)
            idx+=1

            # right
            if vals[idx]!='#':
                node.right = TreeNode(int(vals[idx]))
                q.append(node.right)
            idx+=1
        return root

