class Solution:
    def shortestWay(self, s: str, t: str) -> int:
        
        if not t:
            return 1
        
        if not s:
            return -1
        
        i = j = res = 0
        
        while j< len(t):
            sval = j
            while i<len(s) and j<len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1
            if j == sval:
                return -1
            res += 1            
            i = 0
            
        return res
