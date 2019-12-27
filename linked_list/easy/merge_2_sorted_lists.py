# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        return self.merge(l1, l2)
        
        
    def merge(self, left, right):
        
        if not left:
            return right
        
        if not right:
            return left
        
        l = left
        r = right
        res = None
        
        if l.val <= r.val:
            res = l
        else:
            res = r
            
        while l and r:
            
            if l.val <= r.val:
                
                while l.next and l.next.val <= r.val:
                    l = l.next
                    
                temp = l.next
                l.next = r
                l = temp
                
            else:
                
                while r.next and r.next.val < l.val:
                    r = r.next
                    
                temp = r.next
                r.next = l
                r = temp
                
        return res
        
