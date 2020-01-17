from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        c = Counter(nums)
        return [ele[0] for ele in c.most_common()[:k]]
