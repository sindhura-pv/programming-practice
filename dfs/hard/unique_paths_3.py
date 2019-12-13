from collections import defaultdict as dd
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        res = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        m = len(grid)
        n = len(grid[0])
        zeros = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zeros += 1
                
        def dfs(i, j, vis, z):
            
            if grid[i][j] == 2 and z==zeros:
                nonlocal res
                res += 1
                return
            
            vis[(i,j)] = True
            
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                
                if (x<0 or x>=m or y<0 or y>=n or grid[x][y]==-1 or vis[(x,y)]):
                    continue
                
                dfs(x,y, vis, z+1)
                
            vis[(i,j)] = False
                
            return 
        
        d = dd(bool)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j, d, -1)
        
        return res
                
            
