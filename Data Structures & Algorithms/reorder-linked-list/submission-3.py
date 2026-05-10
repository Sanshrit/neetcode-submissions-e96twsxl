# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return 
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        # reverse second half

        curr = head2
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        t1 = head
        t2 = prev
        while t1 and t2:
            t1_next = t1.next
            t2_next = t2.next
            t1.next = t2
            t2.next = t1_next
            
            t1= t1_next
            t2=t2_next
        
        
        