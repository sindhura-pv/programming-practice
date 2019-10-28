from heapq import nlargest
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        length = len(stones)
        while length>1:
            l, sl = nlargest(2, stones)
            if l == sl:
                stones.remove(l)
            else:
                stones[stones.index(l)] = l-sl
            stones.remove(sl)
            length = len(stones)
            
        return stones[0] if stones else 0
            
