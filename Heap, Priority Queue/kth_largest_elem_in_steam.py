from heapq import heapify, heappop, heappush
from typing import List


class KthLargest:
    heap = None
    size = 0

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        if len(nums) <= k:
            self.heap = nums
        else:
            self.heap = sorted(nums)[-k:]
        heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.size:
            heappush(self.heap, val)
            return self.heap[0]
        if self.heap[0] < val:
            heappop(self.heap)
            heappush(self.heap, val)
            return self.heap[0]
        else:
            return self.heap[0]


obj = KthLargest(4, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
