from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > nums[len(nums) - 1]:
            left = 0
            right = len(nums) - 1
            mid = self.search_min(nums, left, right)
            if target == nums[0]:
                return 0
            if target > nums[0]:
                return self.binary(nums, target, left, mid - 1)
            else:
                return self.binary(nums, target, mid, right)
        else:
            return self.binary(nums, target, 0, len(nums) - 1)

    def binary(self, nums, target, left, right):
        ans = -1
        if abs(left - right) <= 1:
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            return ans
        if nums[left + ((right - left) // 2)] == target:
            return left + ((right - left) // 2)
        if nums[left + ((right - left) // 2)] > target:
            return self.binary(nums, target, left, left + ((right - left) // 2))
        if nums[left + ((right - left) // 2)] < target:
            return self.binary(nums, target, left + ((right - left) // 2), right)

    def search_min(self, nums, left, right):
        if right - left <= 1:
            return right
        mid = left + (right - left) // 2
        if nums[mid] > nums[left]:
            return self.search_min(nums, mid, right)
        if nums[mid] < nums[left]:
            return self.search_min(nums, left, mid)


s = Solution()
print(s.search(nums =
[3,1], target = 3))
