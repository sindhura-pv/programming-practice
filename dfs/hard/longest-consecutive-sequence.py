class Solution:
    def longestConsecutive(self, nums) -> int:

        if not nums:
            return 0

        ns = set(nums)
        vis = set()
        diff = float('-inf')

        def find(num):

            if num in vis or num not in ns:
                return 0

            vis.add(num)
            return find(num - 1) + find(num + 1) + 1

        for num in nums:
            if num not in vis:
                diff = max(diff, find(num))

        return diff

