# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        t1 = dummy
        h1 = list1
        h2 = list2

        while h1 and h2:
            if h1.val <= h2.val:
                t1.next = h1
                t1 = t1.next
                h1 = h1.next
            else:
                t1.next = h2
                t1= t1.next
                h2=h2.next
        
        while h1:
            t1.next = h1
            t1 = t1.next
            h1 = h1.next
        while h2:
            t1.next = h2
            t1 = t1.next
            h2 = h2.next
        return dummy.next               
