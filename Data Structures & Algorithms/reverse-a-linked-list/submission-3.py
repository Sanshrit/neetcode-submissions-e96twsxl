# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = []
        def rev(head):
            if head.next:
                rev(head.next)
            else:
                newHead.append(head)
                return
            nxt = head.next
            nxt.next = head
            head.next = None
        if head is None or head.next is None:
            return head
        rev(head)
        return newHead[0]
        



        

