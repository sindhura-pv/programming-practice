from collections import defaultdict as dd

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if not trust:
            return n
        
        tt = set()
        te = dd(int)
        
        for t in trust:
            tt.add(t[0])
            te[t[1]] += 1
            
        #print(tt, te)
        res = -1
        for i in range(n+1):
            
            if i not in tt and te[i]==n-1:
                res = i
                break
                
        return res
            
       
