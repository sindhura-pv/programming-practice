# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.res = []

    def findLeaves(self, root):
        if not root:
            return []
        self.putLeaves(root)
        return self.res

    def putLeaves(self, node):

        if not node.left and not node.right:
            if len(self.res) < 1:
                self.res.append([node.val])
            else:
                self.res[0].append(node.val)
            return 1

        lv = rv = -1
        if node.left:
            lv = self.putLeaves(node.left)
        if node.right:
            rv = self.putLeaves(node.right)

        v = max(lv, rv)
        if len(self.res) < v + 1:
            self.res.append([node.val])
        else:
            self.res[v].append(node.val)

        return v + 1