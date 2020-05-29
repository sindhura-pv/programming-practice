# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pruneTree(self, root):

        def cutTree(node):

            if not node:
                return 0

            lv = cutTree(node.left)
            if lv == 0:
                node.left = None
            rv = cutTree(node.right)
            if rv == 0:
                node.right = None

            return lv + rv + node.val

        return None if cutTree(root) == 0 else root