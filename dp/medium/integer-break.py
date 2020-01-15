class Solution:
    def integerBreak(self, n: int) -> int:

        memo = dict()
        memo[1] = 1

        def divide(n):

            if n in memo:
                return memo[n]

            prod = -1

            for i in range(n-1,0,-1):
                prod = max(prod, i*divide(n-i), i*(n-i))

            memo[n] = prod
            return prod

        return divide(n)
