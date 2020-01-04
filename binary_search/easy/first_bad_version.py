# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n==1:
            return 1 if isBadVersion(1) else -1
        
        left = 1
        right = n+1
        
        if isBadVersion(left):
            return left
        
        while left<right:
            
            
            
            mid = (left+right)//2
            
            if isBadVersion(mid):
                
                if mid==n and not isBadVersion(mid-1):
                    return mid
                
                elif mid==0 and isBadVersion(mid+1):
                    return mid
                
                elif not isBadVersion(mid-1) and isBadVersion(mid+1):
                    return mid
                
                else:
                    right = mid
                    
            else:
                left = mid + 1
                
        if isBadVersion(left) and isBadVersion(left+1):
            return left
        
        return -1
                
                
            
