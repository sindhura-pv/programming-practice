class Solution:
    def maxSatisfied(self, cus, grumpy, x: int) -> int:

        if not grumpy or not cus:
            return 0

        if x >= len(grumpy):
            return sum(cus)

        sat = 0
        s = 0

        for i in range(x):
            s += cus[i]

        for j in range(x, len(grumpy)):
            s += cus[j] * (1 - grumpy[j])

        sat = s
        for i in range(1, len(grumpy) - x + 1):
            s = s - cus[i - 1] * grumpy[i - 1] + cus[i + x - 1] * grumpy[i + x - 1]
            sat = max(s, sat)

        return sat
