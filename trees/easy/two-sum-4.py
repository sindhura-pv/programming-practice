# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        if not root or (not root.right and not root.left):
            return False

        d = set()

        def find(node, tar):

            if not node:
                return False

            if tar - node.val in d:
                return True

            d.add(node.val)
            return find(node.left, tar) or find(node.right, tar)

        return find(root, k)