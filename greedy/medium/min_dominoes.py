class Solution:
    def minDominoRotations(self, a: List[int], b: List[int]) -> int:
        
        n = len(a)
        nu = 1
        nl = 1
        ru = rl =0
        
        cu = 0
        cl = 0
        for j in range(1,n):
            
            cu += int(a[j]==b[j]==a[0])
            cl += int(a[j]==b[j]==b[0])
            lis = [a[j], b[j]]
            if a[0] not in lis and b[0] not in lis:
                return -1
            
            if a[0] in lis:
                nu += 1
                if lis[0]!=a[0]:
                    ru += 1
                
            if b[0] in lis:
                nl += 1
                if lis[1]!=b[0]:
                    rl += 1
                
        res = float('inf')
        #print(n, nu,nl, ru, rl, count)
        if nu == n:
            res = min(res, min(ru, n-ru-cu))
        if nl == n:
            res = min(res, min(rl, n-rl-cl))
            
        return -1 if res==float('inf') else res
