# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        def isSameTree(p,q):
            queue = deque([(p,q)])
            while queue:
                nodep,nodeq = queue.popleft()
                if not nodep and not nodeq:
                    continue
                if not nodep or not nodeq or nodep.val!=nodeq.val:
                    return False
                queue.append((nodep.left,nodeq.left))
                queue.append((nodep.right,nodeq.right))
            return True
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if isSameTree(node,subRoot):
                return True
            queue.append(node.left)
            queue.append(node.right)
        return False
        """
        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val!=q.val:
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        if not root:
            return False
        if isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
