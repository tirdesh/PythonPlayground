# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        # Single pass to count total nodes (avoids re-checking boundaries per group)
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        group_prev = dummy

        while length >= k:
            # Locate the k-th node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
            group_next = kth.next

            # Reverse pointers within this k-length window
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect: group_prev -> new head (kth); advance to new tail
            new_tail = group_prev.next
            group_prev.next = kth
            group_prev = new_tail

            length -= k

        return dummy.next