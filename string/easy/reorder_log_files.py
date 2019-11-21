class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        lis1 = []
        lis2 = []
        for log in logs:
            words = log.split(' ')
            if not words[1].isdigit():
                lis1.append(( words[0], " ".join(words[1:]) ))
            else:
                lis2.append(log)
                
        lis1.sort(key= lambda x: x[1]+x[0])
        
        res = []
        for ele in lis1:
            res.append(ele[0] + ' ' + ele[1])
            
        return res + lis2
