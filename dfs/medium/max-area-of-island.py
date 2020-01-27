class Solution:
    def maxAreaOfIsland(self, grid) -> int:

        max_area = 0

        def calc_area(grid, x, y):
            m = len(grid)
            n = len(grid[0])

            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
                return 0

            grid[x][y] = 0
            count = 0
            for dir in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
                i, j = x + dir[0], y + dir[1]
                count += calc_area(grid, i, j)

            return count + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    max_area = max(max_area, calc_area(grid, i, j))

        return max_area
