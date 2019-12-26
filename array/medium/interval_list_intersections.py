class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        
        if not a or not b:
            return []
        
        i = j = 0
        
        start = end = 0
        res = []
        
        while i< len(a) and j<len(b):
            
            #print(start, i, j)
            
            start = max(a[i][0], b[j][0])
            end = min(a[i][1], b[j][1])
            
            if start <= end:
                res.append([start, end])
                
            if end == a[i][1]:
                i += 1
            if end == b[j][1]:
                j += 1
            
        return res
