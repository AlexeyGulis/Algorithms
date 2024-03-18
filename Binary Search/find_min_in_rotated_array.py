from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] > nums[len(nums) - 1]:
            return self.searchMin(nums, 0, len(nums) - 1)
        else:
            return nums[0]

    def searchMin(self, nums, left, right):
        if right - left <= 1:
            return nums[right]
        mid = left + (right - left) // 2
        if nums[mid] > nums[left]:
            return self.searchMin(nums, mid, right)
        if nums[mid] < nums[left]:
            return self.searchMin(nums, left, mid)


s = Solution()
print(s.findMin(nums = [4,5,6,7,0,1,2]))
