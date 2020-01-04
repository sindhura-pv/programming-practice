class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if not nums:
            return -1
        
        if len(nums)==1:
            return nums[0]
        
        n = len(nums)
        
        def ispivot(i):
            
            if nums[(i-1)%n] > nums[i]:
                return True
            
            return False
        
        left = 0
        right = n-1
        
        while left < right:
            
            mid = (left+right)//2
            
            if ispivot(mid):
                return nums[mid]
            
            if nums[right] < nums[mid]:
                left = mid +1
                
            else:
                right = mid
                
        if ispivot(left):
            return nums[left]
        
        return -1
            
            
        
