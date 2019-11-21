import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        
        if not sticks:
            return 
        
        cost = 0
        heapq.heapify(sticks)
        
        while len(sticks) > 1:
            st1 = heapq.heappop(sticks)
            st2 = heapq.heappop(sticks)
            
            heapq.heappush(sticks, st1+st2)
            cost = cost + st1 + st2
            
        return cost
            
