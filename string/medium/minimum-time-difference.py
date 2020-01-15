class Solution:
    def findMinDifference(self, t: List[str]) -> int:

        l = []
        for s in t:
            time = int(s.split(":")[0]) * 60 + int(s.split(":")[1])
            l.append(time)

        l.sort()
        curr = float('inf')
        n = len(l)

        for i in range(n - 1):
            new = l[i + 1] - l[i]
            curr = min(curr, new)

        diff = 24 * 60 + l[0] - l[-1]
        curr = min(diff, curr)

        return curr
