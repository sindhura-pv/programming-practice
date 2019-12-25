import numpy as np

class Solution:
    def numRollsToTarget(self, dices: int, faces: int, tar: int) -> int:
        
        if tar < dices or tar> dices*faces:
            return 0
        
        if dices==1:
            return int(tar<=faces)
        
        dp = np.zeros(shape=[dices,tar])
        mod = 10**9 + 7
        
        for f in range(min(faces, tar)):
            dp[0][f] = 1
        
        for d in range(1, dices):
            for i in range(tar):
                for j in range(1, faces+1):
                    
                    if j <= i:
                        dp[d][i] += dp[d-1][i-j]
                        dp[d][i] %= mod
                        
        #print(dp)
                        
        return int(dp[dices-1][tar-1])
