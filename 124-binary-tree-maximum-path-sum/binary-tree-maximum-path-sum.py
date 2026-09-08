# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def get_max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Post-order: recursively compute max gain from subtrees.
            # Clamp negative gains to 0 (ignore branches that reduce sum).
            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))

            # Current node as the highest point (turning point) of a path
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            # Return max single-branch gain extending up to parent
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return max_sum