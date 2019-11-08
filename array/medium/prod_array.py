class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return 
        
        f = [1]*len(nums)
        s = [1]*len(nums)
        prod = [1]*len(nums)
        
        for i in range(1, len(nums)):
            f[i] = f[i-1]*nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            s[i] = s[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            prod[i] = f[i]*s[i]
            
        return prod
