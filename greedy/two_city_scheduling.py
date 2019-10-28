class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        if not costs:
            return 0
        
        n = len(costs)
        costs.sort(key=lambda x: x[0]-x[1])
        ca = sum([k[0] for k in costs[:n//2]])
        cb = sum([k[1] for k in costs[n//2:]])
        return ca + cb
                
