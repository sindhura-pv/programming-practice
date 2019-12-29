# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        if (not root.left and not root.right):
            return [root.val]
        
        que = []
        res = []
        
        que.append(root)
        l = len(que)
        
        while que:
            
            for i in range(l):
                node = que.pop(0)
                if i==l-1:
                    res.append(node.val)
                    
                if node.left:
                    que.append(node.left)
                    
                if node.right:
                    que.append(node.right)
                    
            l = len(que)
            
        return res
