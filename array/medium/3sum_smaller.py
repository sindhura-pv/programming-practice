class Solution:

    def threeSumSmaller(self, nums, target: int) -> int:

        if len(nums) < 3:
            return 0

        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 2):
            tar = target - nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] < tar:
                    count += (k - j)
                    j += 1
                else:
                    k -= 1

        return count
