class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1

        return self.find(nums, target)
        
        
    def find(self, nums, tar):
        
        i = 0
        low = 0
        high = len(nums)-1
        mid = -1
        n = len(nums)
        
        while low <= high:
            
            mid = (low+high)//2
            
            if nums[mid] == tar:
                return mid
            
            
            elif nums[low] <= nums[mid]:
                if tar>= nums[low] and tar<nums[mid]:
                    high = mid -1
                else:
                    low = mid +1
                
            else:
                if tar <= nums[high]  and tar > nums[mid]:
                    low = mid + 1
                else:
                    high = mid -1
                

                
        return -1
