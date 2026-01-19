# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            dummy = ListNode(head.val)
        else:
            return head
        current = head
        temp = dummy
        while current:
            if temp.val==current.val:
                current = current.next
            else:
                temp.next = ListNode(current.val)
                temp = temp.next
        return dummy
                

