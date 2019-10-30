class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        if not arr or 0 not in arr:
            return
        
        l = len(arr)
        i =0
        while i<l:
            
            if arr[i] == 0:
                j = i+1
                temp = 0
                while j<l:
                    pholder = arr[j]
                    arr[j] = temp
                    temp = pholder
                    j += 1
                i += 1
                
            i += 1
                            
        return
