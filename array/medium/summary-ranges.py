class Solution:
    def summaryRanges(self, nums):

        if not nums:
            return []

        st = str(nums[0])
        num = nums[0]
        result = []

        for i in range(1, len(nums)):

            if num == nums[i] - 1:
                num = nums[i]

            else:

                if int(st) != num:
                    result.append(st + "->" + str(num))
                else:
                    result.append(st)

                num = nums[i]
                st = str(nums[i])

        if int(st) != num:
            result.append(st + "->" + str(num))
        else:
            result.append(st)

        return result
