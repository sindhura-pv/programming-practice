from collections import defaultdict as dd

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
        vis = dd(bool)
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            a = i
            b = i+1
            c = len(nums)-1
            
            while b<c:
                #print(nums[a], nums[b], nums[c])
                if nums[a]+ nums[b]+ nums[c] < 0:
                    b += 1
                    
                elif nums[a]+ nums[b]+ nums[c] > 0:
                    c -= 1
                    
                else:
                    if not vis[(nums[a], nums[b], nums[c])]:
                        res.append([nums[a], nums[b], nums[c]])
                        vis[(nums[a], nums[b], nums[c])] = True
                    b += 1
                    c -= 1
                        
        return res
