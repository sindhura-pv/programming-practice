
class Solution:
    def kthSmallest(self, matrix, k):
        arr = []
        for row in matrix:
            arr = arr + row
        return sorted(arr)[k - 1]
