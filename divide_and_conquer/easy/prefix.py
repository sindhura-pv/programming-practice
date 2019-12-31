
class Solution:

    def prefix(self, strs):
        return lcp(strs, 0, len(strs)-1)

    def lcp(self, strs, i, j):

        if i==j:
            return strs[i]

        mid = (i+j)//2
        l = self.lcp(strs, i, mid)
        r = self.lcp(strs, mid+1, j)

        return self.lcp_util(l, r)

    def lcp_util(self, l, r):

        res = ""
        n = min(len(l), len(r))

        for i in range(n):
            if l[i] == r[i]:
                res += l[i]

            else:
                break

        return res

