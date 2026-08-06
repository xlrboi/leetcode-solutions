# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        l = 0
        last = head
        while last.next is not None:
            last = last.next
            l += 1
        l += 1

        k = k%l
        if k == 0:
            return head
        
        curr = head
        for _ in range(l-k-1):
            curr = curr.next

        last.next = head
        head = curr.next
        curr.next = None
        return head