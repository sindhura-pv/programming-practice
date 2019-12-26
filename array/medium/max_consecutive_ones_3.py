class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        
        if not a:
            return 0
        
        if k == 0:
            res  = count = 0
            for ele in a:
                count = count + 1 if ele==1 else 0
                res = max(res, count)
            return res
        
        start = end = 0
        res = -1
        zeros = k
        
        for i in range(len(a)):
            
            #print(i, start, end)
            
            if a[i] == 0:
                
                if zeros > 0:
                    zeros -= 1
                    
                else:
                    res = max(res, end - start + 1)
                    while a[start] == 1 and start <= end:
                        start += 1
                        
                    if start != end:
                        start += 1
                
            end = i
            
        res = max(res, end - start + 1)
        
        return res
