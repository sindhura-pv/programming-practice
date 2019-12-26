from collections import defaultdict as dd

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
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
