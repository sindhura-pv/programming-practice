# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        return self.mergeSort(head)
    
    def mergeSort(self, head):
        
        if not head or not head.next:
            return head
        
        mid = self.getMiddle(head)
        nextMid = mid.next
        mid.next = None
        
        left = self.mergeSort(head)
        right = self.mergeSort(nextMid)
        
        return self.merge(left, right)
    
    def getMiddle(self, head):
        
        if not head:
            return head
        
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
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
                    
            
        
