class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])
        vis = {}
        for i in range(m):
            vis[i] = False
        
        def findTotal(x):
            
            for y in range(n):
                if mat[x][y] == 1 and not vis[y]:
                    vis[y] = True
                    findTotal(y)
            
            return 
        
        res = 0
        for i in range(m):
            if not vis[i]:
                findTotal(i)
                res += 1
        return res
