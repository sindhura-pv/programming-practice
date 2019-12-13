class Solution:
    def searchRange(self, nums: List[int], tar: int) -> List[int]:
        
        if not nums:
            return [-1,-1]
        
        a = 0
        b = len(nums)-1
        lis = []
        
        while a<=b:
            mid = (a+b)//2
            if nums[mid]==tar:
                
                if mid==0 or nums[mid-1]<tar:
                    a = mid
                    lis.append(a)
                    break
                else:
                    b = mid-1
                    
            elif nums[mid]<tar:
                a = mid+1
                
            else:
                b = mid-1
                
        if a>b:
            return [-1,-1]
        
        
        b = len(nums)-1
        
        while a<=b:
            mid = (a+b)//2
            if nums[mid] == tar:
                if mid == len(nums)-1 or nums[mid+1]>tar:
                    b = mid
                    lis.append(b)
                    break
                else:
                    a = mid+1
                    
            elif nums[mid]> tar:
                b = mid-1
                
            else:
                a = mid+1
                
        return lis
