import numpy as np

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dp =[]
        
        dp = np.zeros(shape = [m+1, n+1])
                
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i+1][j+1] = grid[i][j]
                elif i==0:
                    dp[i+1][j+1] = dp[i+1][j] + grid[i][j]
                elif j==0:
                    dp[i+1][j+1] = dp[i][j+1] + grid[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + grid[i][j]
                
        #print(dp)
                
        return int(dp[m][n])

        
        
