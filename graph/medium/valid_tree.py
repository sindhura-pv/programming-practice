from collections import defaultdict as dd

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True

        if len(edges) != n-1:
            return False
        
        d = dd(list)
        vis = set()
        
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
            
        
        def dfs(node, vis):
            
            if node in vis:
                return
            
            vis.add(node)
            for neigh in d[node]:
                dfs(neigh, vis)
                
        
        res = dfs(0, vis)
            
        return len(vis) == n
