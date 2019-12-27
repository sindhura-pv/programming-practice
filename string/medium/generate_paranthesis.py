class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def bktk(s, i_temp, i_total):
            
            if len(s) == 2*n-1:
                res.append(s + ')')
                return
            
            if i_temp > 0:
                bktk(s + ')', i_temp-1, i_total)
                
            if i_total < n:
                bktk(s + '(', i_temp+1, i_total+1)
              
        bktk("", 0, 0)
         
        return res
