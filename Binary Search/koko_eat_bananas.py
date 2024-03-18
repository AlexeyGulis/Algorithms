import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r1 = 0
        my_list = sorted(piles)
        if len(my_list) == 1:
            return math.ceil(my_list[0] / h)
        if self.evaluate_hours(my_list, 1) <= h:
            return 1
        r1 = self.binary(my_list, 1, my_list[len(my_list) - 1], h)
        return r1

    def evaluate_hours(self, nums, key):
        ans = 0
        for num in nums:
            ans += math.ceil(num / key)
        return ans

    def binary(self, nums, left, right, target):
        if right - left <= 1:
            return right
        median_sum = self.evaluate_hours(nums, left + (right - left) // 2)
        if median_sum <= target:
            return self.binary(nums, left, left + (right - left) // 2, target)
        if median_sum > target:
            return self.binary(nums, left + (right - left) // 2, right, target)


s = Solution()
print(s.minEatingSpeed([2, 2], h = 4))
