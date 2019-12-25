from collections import defaultdict as dd 
import numpy as np

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        dp = dd(dict)
        n = len(nums)
        
        def dfs(i, s, tar):
            
            if i == n-1:
                dp[i][s + nums[i]] = int(s + nums[i] == tar)
                dp[i][s - nums[i]] = int(s - nums[i] == tar)
                return dp[i][s + nums[i]] + dp[i][s - nums[i]]
            
            if not dp[i]:
                dp[i] = dd(int)
            
            if not dp[i][s + nums[i]]:
                dp[i][s + nums[i]] = dfs(i+1, s+nums[i], tar)
                
            if not dp[i][s - nums[i]]:
                dp[i][s - nums[i]] = dfs(i+1, s-nums[i], tar)
            
            return dp[i][s + nums[i]] + dp[i][s - nums[i]]
        
        return dfs(0, 0, S)
                
       
