"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None

        
        res = cur = None
        prev = None
        d = dict()
        
        while head:
            
            if head in d:
                cur = d[head]
                
            else:
                cur = Node(head.val, None, None)
                d[head] = cur
                
            if prev:
                prev.next = cur
                
            if head.random:
                if head.random in d:
                    cur.random = d[head.random]
                else:
                    cur.random = Node(head.random.val, None, None)
                    d[head.random] = cur.random
                    
            if not res:
                res = cur
                
            prev = cur
            head = head.next
        
        return res
