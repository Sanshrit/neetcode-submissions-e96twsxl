"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m1 = {}
        m1[None] = None

        temp = head
        

        while temp:
            m1[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        newHead = m1[temp]

        while temp:
            m1[temp].next = m1[temp.next]
            m1[temp].random = m1[temp.random]
            temp = temp.next
        
        return newHead

        