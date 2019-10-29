class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if len(points) < 2:
            return len(points)
        
        points.sort(key=lambda x: x[1])
        end = points[0][1]
        res = 1
        
        for s,e in points[1:]:
            if s>end:
                end = e
                res += 1
                
        return res
