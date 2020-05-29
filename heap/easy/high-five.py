import heapq


class Solution:
    def highFive(self, items):

        d = {}
        result = []
        for item in items:
            if item[0] not in d:
                d[item[0]] = []
                heapq.heapify(d[item[0]])
            heapq.heappush(d[item[0]], item[1])

        for k in d:
            scores = heapq.nlargest(5, d[k])
            result.append([k, int(sum(scores) / len(scores))])

        result.sort(key=lambda x: x[0])

        return result