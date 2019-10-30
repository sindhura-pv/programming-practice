class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        rmin = float('inf')
        lmax = float('-inf')
        
        def func(node, l, r):
            
            if not node:
                return True
            
            val = node.val
            if val<=l or val>=r:
                return False
            
            if not func(node.left, l, val):
                return False
            
            if not func(node.right, val, r):
                return False
            
            return True
        
        return func(root, lmax, rmin)
