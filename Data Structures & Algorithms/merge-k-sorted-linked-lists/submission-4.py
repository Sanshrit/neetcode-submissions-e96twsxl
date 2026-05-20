# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy

        heap = []
        cnt = 0
        for node in lists:
            heapq.heappush(heap,(node.val,cnt,node))
            cnt+=1
        
        while heap:
            value,i,nd = heapq.heappop(heap)
            if nd.next:
                heapq.heappush(heap,(nd.next.val,i,nd.next))
            temp.next = nd
            temp = temp.next
        return dummy.next