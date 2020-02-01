class Solution:
    def combinationSum(self, candidates, target: int):

        res = []
        vis = set()

        def calc_sum(arr, sum, input, tar):

            if sum > tar:
                return

            nonlocal res
            nonlocal vis
            for num in input:
                if sum + num == tar and tuple(sorted(arr + [num])) not in vis:
                    res.append(arr + [num])
                    vis.add(tuple(sorted(arr + [num])))
                    return
                calc_sum(arr + [num], sum + num, input, tar)

        if not candidates:
            return []

        candidates.sort()
        calc_sum([], 0, candidates, target)
        return res
