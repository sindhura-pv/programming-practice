class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        a = version1.split('.')
        b = version2.split('.')
        if len(a) > len(b):
            b = b + [0]*(len(a)-len(b))
        else:
            a = a + [0]*(len(b)-len(a))
        for i in range(len(a)):
            if int(a[i]) < int(b[i]):
                return -1
            elif int(a[i]) > int(b[i]):
                return 1
        return 0
