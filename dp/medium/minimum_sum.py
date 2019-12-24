class Solution:
    def numSquares(self, n: int) -> int:
        
        nums = []
        
        for i in range(1, n+1):
            
            if i*i < n:
                nums.append(i*i)
                
            elif i*i == n:
                return 1
            
            else:
                break
                
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        for num in nums:
            for x in range(num, n+1):
                dp[x] = min(dp[x], dp[x-num] + 1)
                
        return dp[n]
