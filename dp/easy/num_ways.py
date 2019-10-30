class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n==0 or k==0:
            return 0
        if n==1:
            return k
        if k==1:
            if n<3:
                return k
            return 0    
        
        dp = [k, k*k]
        
        for j in range(2, n):
            temp = dp[-1]*k
            x = -1
            for i in range(len(dp)-2, -1, -1):
                temp += x*dp[i]
                x *= -1
            dp.append(temp)
            
        #print(dp)
        return dp[-1]
