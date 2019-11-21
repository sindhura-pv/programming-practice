from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        que = deque()
        m = len(mat)
        n = len(mat[0])
        vis = {}
        res = []
        dirs = {(-1,0),(0,-1),(1,0),(0,1)}
        
        for i in range(m):
            res.append([float('inf')]*n)
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i,j))
                    vis[(i,j)] = True
                else:
                    vis[(i,j)] = False
              
        level = 0
        l = len(que)
        
        while que:
            for k in range(l):
                i,j = que.popleft()
                res[i][j] = level
                
                for d in dirs:
                    nx = i + d[0]
                    ny = j + d[1]
                    
                    if (nx<0 or nx>=m or ny<0 or ny>=n or vis[(nx,ny)]):
                        continue
                        
                    que.append((nx,ny))
                    vis[(nx,ny)] = True
                    
            level += 1
            l = len(que)
            
        return res
