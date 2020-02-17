class Solution:
    def maxProduct(self, a) -> int:

        if not a:
            return 0

        if len(a) == 1:
            return a[0]

        mx = mn = prod = a[0]

        for i in range(1, len(a)):
            temp = mx
            mx = max(max(mx * a[i], mn * a[i]), a[i])
            mn = min(min(temp * a[i], mn * a[i]), a[i])
            prod = max(prod, mx)

        return prod
