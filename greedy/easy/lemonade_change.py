class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        cfive = cten = 0
        if not bills:
            return True
        
        for i in range(len(bills)):
            if bills[i] == 5:
                cfive += 1
                
            if bills[i] == 10:
                cten += 1
                if cfive ==0:
                    return False
                else:
                    cfive -= 1
                    
            if bills[i] == 20:
                if cfive == 0 or (cten==0 and cfive<3):
                    return False
                if cten ==0:
                    cfive -= 3
                else:
                    cten -= 1
                    cfive -= 1
                
                    
        return True
