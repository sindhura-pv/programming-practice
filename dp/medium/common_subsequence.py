class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        
        m = len(t1)
        n = len(t2)
        dp = []
        
        for i in range(m+1):
            temp = [0]*(n+1)
            dp.append(temp)
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if t1[i-1] == t2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[-1][-1]
