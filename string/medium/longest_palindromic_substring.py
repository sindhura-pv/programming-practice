class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        
        if s == s[::-1]:
            return s
        
        def func(s, l, r):
            n = len(s)
            
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
                
            return r-l-1
                
        
        n = len(s)
        length = -1
        res = ""
        
        for i in range(n):
            
            l1 = func(s, i, i)
            l2 = func(s, i, i+1)
            tot = max(l1, l2)
            
            if tot > length:
                length = tot
                res = s[(i-(tot-1)//2): (i + tot//2)+1]
            
        return res
                        

                        
                    
        
