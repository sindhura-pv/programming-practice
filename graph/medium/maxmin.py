class Solution:
    def maximumMinimumPath(self, a: List[List[int]]) -> int:
    
        
        vis = set()
        max_score = float('-inf')
        m = len(a)
        n = len(a[0])
        dirs = {(0,1),(1,0),(-1,0),(0,-1)}
        
        def maxmin(i, j, vis, mini):
            
            if i<0 or j<0 or i>=m or j>=n:
                return
            
            mini = min(mini, a[i][j])
            
            if i== m-1 and j==n-1:
                nonlocal max_score
                max_score = max(max_score, mini)
                return
            
            vis.add((i,j))
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                if (x,y) not in vis:
                    maxmin(x, y, vis, mini)
                    
            vis.remove((i,j))
            
            return
        
        maxmin(0,0,vis, float('inf'))
        return max_score
        
