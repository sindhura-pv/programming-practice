class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        sm = 0
        l = 0
        r = 0
        ml = float('inf')
        
        while r<len(nums):
            sm += nums[r]
            while l<=r and sm>=s:
                ml = min(ml, r-l+1)
                sm -= nums[l]
                l += 1
                
            r += 1
            
        return ml if ml!= float('inf') else 0
            
