class Solution:
    def longestIncreasingPath(self, mat) -> int:

        if not mat:
            return 0

        dp = dict()

        def find(i, j, m, n, vis):

            if (i, j) in dp:
                return dp[(i, j)]

            vis.add((i, j))
            count = 0

            for x, y in {(-1, 0), (0, -1), (1, 0), (0, 1)}:

                nx, ny = i + x, j + y
                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in vis or mat[nx][ny] >= mat[i][j]:
                    continue

                count = max(count, find(nx, ny, m, n, vis))

            vis.remove((i, j))

            dp[(i, j)] = count + 1
            return dp[(i, j)]

        m = len(mat)
        n = len(mat[0])
        l = 0

        for i in range(m):
            for j in range(n):
                l = max(l, find(i, j, m, n, set()))

        return l




