class Solution:
    def threeSumClosest(self, nums: List[int], tar: int) -> int:
        
        if not nums:
            return []
        
        diff = float('inf')
        s = 0
        nums.sort()
        
        for i in range(len(nums)-2):
            a = i
            b = i+1
            c = len(nums)-1
            
            while b<c:
                if nums[a]+ nums[b]+ nums[c] < tar:
                    if abs(tar- (nums[a]+ nums[b]+ nums[c])) < diff:
                        diff = abs(tar- (nums[a]+ nums[b]+ nums[c]))
                        s = nums[a]+ nums[b]+ nums[c]
                    b += 1
                    
                elif nums[a]+ nums[b]+ nums[c] > tar:
                    if abs(tar- (nums[a]+ nums[b]+ nums[c])) < diff:
                        diff = abs(tar- (nums[a]+ nums[b]+ nums[c]))
                        s = nums[a]+ nums[b]+ nums[c]
                    c -= 1
                    
                else:
                    return tar
                        
        return s
