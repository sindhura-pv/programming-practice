# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q) -> bool:

        if not p and not q:
            return True

        elif not p:
            return False

        elif not q:
            return False

        elif p.val != q.val:
            return False

        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
