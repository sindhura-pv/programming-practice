class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        lc = res = ""
        
        while a!=0 or b!=0:
            
            if a>=b:
                if lc != 'a':
                    res += 'a'*min(2,a)
                    a -= min(2,a)
                    lc = 'a'
                else:
                    res += 'b'
                    b -= 1
                    lc = 'b'
                    
            else:
                if lc != 'b':
                    res += 'b'*min(2,b)
                    b -= min(2,b)
                    lc = 'b'
                else:
                    res += 'a'
                    a -= 1
                    lc = 'a'
                
        return res
