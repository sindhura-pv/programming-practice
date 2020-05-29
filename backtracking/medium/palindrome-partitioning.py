class Solution:
    def partition(self, s: str):

        res = []

        def find_partitions(st, i, arr):

            nonlocal res
            if i == len(st):
                res.append(arr)
                return

            for j in range(i + 1, len(st) + 1):
                if st[i:j] == st[i:j][::-1]:
                    find_partitions(st, j, arr + [st[i:j]])

        if not s:
            return []

        find_partitions(s, 0, [])
        return res