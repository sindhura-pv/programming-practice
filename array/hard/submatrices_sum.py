from collections import defaultdict as dd

class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], tar: int) -> int:
        
        def subarraySum(nums, k):
        
            if not nums:
                return 0
        
            if len(nums)==1:
                return int(nums[0]==k)
        
            n = len(nums)
            d = dd(int)
            d[0] = 1
            count = sums = 0
        
            for i in range(n):
                sums += nums[i]
                count += d[sums-k]
                d[sums] += 1        
                    
            return count
        
        m = len(mat)
        n = len(mat[0])
        a = [0]*m
        count = 0
        
        for i in range(n):
            for j in range(i+1, n+1):
                
                for k in range(m):
                    a[k] = sum(mat[k][i:j])
                    
                count += subarraySum(a, tar)
                
        return count
                
