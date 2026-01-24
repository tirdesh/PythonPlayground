# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None
        dummy = ListNode(0)
        res = dummy
        p,q = list1,list2
        while p or q:
            if p is not None and q is not None:
                if p.val<=q.val:
                    dummy.next = ListNode(p.val)
                    p=p.next
                else:
                    dummy.next = ListNode(q.val)
                    q=q.next
            elif p:
                dummy.next = p
                p=None
            elif q:
                dummy.next = q
                q=None
            dummy=dummy.next
        return res.next

                




        