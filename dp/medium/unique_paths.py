import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp =[]
        
        dp = np.zeros(shape = [m+1, n+1])
                
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i+1][j+1] = 1
                else:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
                
        #print(dp)
                
        return int(dp[m][n])
