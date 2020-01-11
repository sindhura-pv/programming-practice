class Solution:
    def firstMissingPositive(self, nums) -> int:

        s = set()
        num = 1

        for i in range(len(nums)):

            s.add(nums[i])

            if nums[i] == num:
                num += 1
                while num in s:
                    num += 1

        return num
