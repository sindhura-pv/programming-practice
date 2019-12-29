# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        ans = None
        count = 0
        
        def find_k(node, k):
            
            if not node:
                return
            
            nonlocal count            
            if node.left:
                find_k(node.left, k)
                
            
            count += 1
            if count == k:
                nonlocal ans
                ans = node.val
                return
            
            if node.right:
                find_k(node.right, k)
                
        find_k(root, k)
        return ans
