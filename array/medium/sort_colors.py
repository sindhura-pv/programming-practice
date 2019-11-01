class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        l = 0
        r = len(nums)-1
        curr = 0
        
        while curr <= r:
            if nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                l += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
                
            elif nums[curr] == 2:
                nums[r], nums[curr] = nums[curr], nums[r]
                r -= 1
                
        return 
