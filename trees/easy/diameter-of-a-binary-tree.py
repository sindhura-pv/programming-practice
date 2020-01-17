# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root) -> int:

        if not root or (not root.left and not root.right):
            return 0

        res = -1

        def findMaxHeight(node):

            if not node:
                return 0

            lv = findMaxHeight(node.left)
            rv = findMaxHeight(node.right)
            val = lv + rv

            nonlocal res
            res = max(res, val)
            return max(lv, rv) + 1

        findMaxHeight(root)
        return res
