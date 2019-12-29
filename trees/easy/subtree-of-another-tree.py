# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if not s or not t:
            return False
        
        def preorder(root, st):
            
            if not root:
                st += 'N'
                return st
            
            st = st + '#' + str(root.val)
            st = preorder(root.left, st)
            st = preorder(root.right, st)
            
            return st
            
        st1 = preorder(s, "")
        st2 = preorder(t, "")
        #print(st1, st2)

        return (st2 in st1)
