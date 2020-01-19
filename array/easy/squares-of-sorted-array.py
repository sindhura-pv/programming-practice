class Solution:

    def sortedSquares(self, a):
        a.sort(key=lambda x: abs(x))
        result = []
        for number in a:
            result.append(number ** 2)

        return result
