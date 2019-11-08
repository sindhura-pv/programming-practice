class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if not s:
            return -1
    
        d = {}
        
        for i,ch in enumerate(s):
            if ch in d:
                d[ch] = float('inf')
            else:
                d[ch] = i
                
        m = float('inf')
        for ele in d:
            if d[ele]<m:
                m = d[ele]
                
        return -1 if m==float('inf') else m
        
        
        
