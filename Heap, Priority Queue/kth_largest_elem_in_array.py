from heapq import heapify, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(len(nums) - k):
            heappop(nums)
        return nums[0]


s = Solution()
print(s.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
