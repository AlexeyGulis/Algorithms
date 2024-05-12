from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        return max(self.help_rob(nums[0:len(nums) - 1]), self.help_rob(nums[1:]))
    def help_rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        my_sum = [0 for i in range(len(nums))]
        my_sum[0] = nums[0]
        my_sum[1] = nums[1]
        for i in range(2, len(nums)):
            if i == 2:
                my_sum[i] = nums[i] + my_sum[i - 2]
            else:
                my_sum[i] = max(nums[i] + my_sum[i - 2], nums[i] + my_sum[i - 3])

        return max(my_sum[len(my_sum) - 1], my_sum[len(my_sum) - 2])


s = Solution()
print(s.rob(nums = [1,2,3,1]))