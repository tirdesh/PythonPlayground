# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        def get_kth(curr: Optional[ListNode], k: int) -> Optional[ListNode]:
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            # Reverse the k nodes between group_prev and group_next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Reconnect group_prev to new head, and advance group_prev
            new_group_tail = group_prev.next
            group_prev.next = kth
            group_prev = new_group_tail

        return dummy.next