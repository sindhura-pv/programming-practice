# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if not head or not head.next:
            return None
        
        prev = last = first = head
        
        for i in range(n):
                last = last.next
                
        if not last:
            return head.next
        
        while last:
            
            prev = first
            first = first.next
            last = last.next
            
        prev.next = first.next
        
        return head
            
            
                
            
        
