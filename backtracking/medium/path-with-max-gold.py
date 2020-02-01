class Solution:
    def getMaximumGold(self, grid) -> int:

        def find_gold_path(grid, dp, i, j, path):

            m = len(grid)
            n = len(grid[0])

            if i >= m or j >= n or i < 0 or j < 0 or (i, j) in path:
                return 0

            # print(i,j)

            if grid[i][j] == 0:
                return 0

            path.add((i, j))
            val = max([find_gold_path(grid, dp, i + x, j + y, path) for x, y in {(-1, 0), (0, -1), (1, 0), (0, 1)}]) + \
                  grid[i][j]
            path.remove((i, j))

            return val

        m = len(grid)
        n = len(grid[0])
        result = -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = find_gold_path(grid, [], i, j, set())
                result = max(result, val)

        return result
