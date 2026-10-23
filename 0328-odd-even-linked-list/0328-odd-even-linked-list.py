class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        temp = head
        values = []

        while temp is not None:
            values.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next

        temp = head.next

        while temp is not None:
            values.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next

        temp = head
        index = 0

        while temp is not None:
            temp.val = values[index]
            index += 1
            temp = temp.next

        return head