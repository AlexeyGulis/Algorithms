from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        my_sum = sum(nums)
        if my_sum % 2 != 0 or max(nums) > my_sum / 2:
            return False
        target = my_sum // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            temp = set()
            for t in dp:
                temp.add(t + nums[i])
                temp.add(t)
            dp = temp

        return True if target in dp else False


s = Solution()
print(s.canPartition(nums = [1,2,3,5]))
