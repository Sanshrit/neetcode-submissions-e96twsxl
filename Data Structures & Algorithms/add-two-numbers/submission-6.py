# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        temp = dummyHead
        sum = 0
        carry=0

        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum//10
            sum = sum%10
            temp.next = ListNode(sum)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            carry = sum//10
            sum = sum%10
            temp.next = ListNode(sum)
            temp = temp.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            carry = sum//10
            sum = sum%10
            temp.next = ListNode(sum)
            temp = temp.next
            l2 = l2.next
        if carry:
            temp.next = ListNode(carry)
        return dummyHead.next                    


