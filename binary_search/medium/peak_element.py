class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if not nums:
            return -1
        
        if len(nums) == 1:
            return 0
        
        def ispeak(i):
            
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return True
            return False
        
        nums = [float('-inf')] + nums + [float('-inf')]
        n = len(nums)
        
        left = 1
        right = n-1
        
        while left+1 < right:
            
            mid = (left+right)//2
            
            if ispeak(mid):
                return mid-1
            
            if nums[mid+1] > nums[mid]:
                left = mid
                
            else:
                right = mid
                
        if ispeak(left):
            return left-1
        
        if ispeak(right):
            return right -1
        
        
        return -1
            
            
        
        
