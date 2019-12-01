from collections import defaultdict as dd

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def sort_str(s):
            lis = list(s)
            lis.sort()
            return ''.join(lis)
        
        if not strs:
            return []
        
        res = dd(list)
        for s in strs:
            res[sort_str(s)].append(s)
            
        return res.values()
