from collections import defaultdict as dd
class Solution:
    def canVisitAllRooms(self, r: List[List[int]]) -> bool:
        
        if not r:
            return True
        
        rooms = set()
        d = dd(list)
        vis = set()
        
        for i in range(len(r)):
            rooms.add(i)
            for room in r[i]:
                d[i].append(room)
                rooms.add(room)
                
        #print(d)
                
        def dfs(node, vis):
            
            if node in vis:
                return
            
            vis.add(node)
            for n in d[node]:
                dfs(n, vis)
                
            return
        
        dfs(0, vis)
        #print(vis, rooms)
        
        return len(vis) == len(rooms)
