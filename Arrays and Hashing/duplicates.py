from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


sol = Solution()

print(sol.containsDuplicate([1, 2, 3, 1]))
print(sol.containsDuplicate([1, 2, 3, 4]))
print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
