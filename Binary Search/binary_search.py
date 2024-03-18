from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        if target < nums[0] or target > nums[len(nums) - 1]:
            return ans
        ans = self.binary(nums, target, 0, len(nums) - 1)
        return ans

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



s = Solution()
print(s.search(nums = [-1,0,3,5,9,12], target = 3))
