class Solution:
    def numDistinctIslands(self, grid) -> int:

        def traverse(i, j, r, c):

            grid[i][j] = 0
            shape.add((i - r, j - c))

            for x, y in {(-1, 0), (0, -1), (1, 0), (0, 1)}:

                nx = i + x
                ny = j + y

                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == 0:
                    continue

                traverse(nx, ny, r, c)

        count = 0
        shapes = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    shape = set()
                    traverse(i, j, i, j)
                    shapes.add(frozenset(shape))

        return len(shapes)

