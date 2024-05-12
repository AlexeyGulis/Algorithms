from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


s = Solution()
print(s.lengthOfLIS(nums =
[0,1,0,3,2,3]))
