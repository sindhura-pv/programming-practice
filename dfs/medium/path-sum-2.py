# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum: int):

        result = []

        def findPaths(node, path, path_sum, sum):

            nonlocal result
            if not node:
                return

            if not node.left and not node.right:
                if path_sum + node.val == sum:
                    result.append(path + [node.val])
                return

            if node.left:
                findPaths(node.left, path + [node.val], path_sum + node.val, sum)
            if node.right:
                findPaths(node.right, path + [node.val], path_sum + node.val, sum)

        findPaths(root, [], 0, sum)
        return result
