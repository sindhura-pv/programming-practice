import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.arr = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
        return self.arr[0]
