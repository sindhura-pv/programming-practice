from collections import defaultdict as dd

class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s=='0' or s[0] == '0':
            return 0
        
        elif len(s)<2:
            return 1
        
                
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '0':
                return 0
        
        n = len(s)
        ans = 0
        dp = dd(int)
        
        dp[len(s)-1] = int(s[-1] != '0')
        dp[len(s)-2] = dp[len(s)-1]
        if int(s[n-2:]) <= 26:
            dp[len(s)-2] += 1
        
        def decode(s, i):
            
            if dp[i]:
                return dp[i]
            
            #print(i)
            
            if s[i] == '0':
                dp[i] = 0
                return dp[i]
            
            if s[i+1] != '0':
                #print("i+1", i)
                dp[i] += decode(s, i+1)
            
            if i<n-1 and int(s[i:i+2]) <= 26:
                #print("i+2", i)
                dp[i] += decode(s, i+2)
                
            return dp[i]
                
        return decode(s, 0)
