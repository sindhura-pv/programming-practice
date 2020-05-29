
class Solution:
    def findLength(self, a, b) -> int:

        m = len(a)
        n = len(b)

        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        res = -1

        for i in range(1, m+1):
            for j in range(1, n+1):

                dp[i][j] = dp[i-1][j-1] + 1 if a[i-1] == b[j-1] else 0
                res = max(res, dp[i][j])

        return res
