class Solution:
        
    def maxSubArray(self, nums):

        return self.calc(nums, 0, len(nums)-1)

    def calc(self, nums, i, j):

        if i==j:
            return nums[i]

        mid = (i+j)//2

        l = self.calc(nums, i, mid)
        r = self.calc(nums, mid+1, j)
        c = self.center(nums, i, mid, j)
        return max(l, r, c)

    def center(self, nums, l, mid, r):

        print("center", l, r, mid)
        i = mid
        j = mid+1

        ls = float('-inf')
        rs = float('-inf')
        ltemp = 0
        rtemp = 0


        while i>=l:
            
            ltemp += nums[i]
            if ltemp>ls:
                ls = ltemp
            i -= 1
                
        while j<=r:
            rtemp += nums[j]
            if rtemp > rs:
                rs = rtemp

            j += 1
            
        return ls + rs
