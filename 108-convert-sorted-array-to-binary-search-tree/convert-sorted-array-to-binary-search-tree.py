# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def middleone(left,right):
            if left>right:
                return None
            mid = left+(right-left)//2
            node = TreeNode(nums[mid])
            node.left = middleone(left,mid-1)
            node.right = middleone(mid+1,right)
            return node
        return middleone(0,len(nums)-1)