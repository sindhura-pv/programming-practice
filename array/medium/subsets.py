class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def func(lis, i, res):
            
            if i>= len(nums):
                return res

            for j in range(i, len(nums)):
                res.append(lis+[nums[j]])
                func(lis + [nums[j]], j+1, res)
                
            return res
        
        return func([], 0, [[]])
