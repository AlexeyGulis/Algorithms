from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = None
        dp = {}
        for i in range(len(nums)):
            if i == 0:
                dp[i] = [nums[i], nums[i]]
                continue
            if nums[i] == 0:
                dp[i] = [0, 0]
                continue
            if dp[i - 1][0] == 0:
                dp[i] = [nums[i], nums[i]]
                continue
            dp[i] = [max(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i]),
                     min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])]

        for k,v in dp.items():
            if answer is None:
                answer = max(v[0], v[1])
            else:
                if answer < max(v[0], v[1]):
                    answer = max(v[0], v[1])

        return answer


s = Solution()
print(s.maxProduct([-1,4,-4,5,-2,-1,-1,-2,-3]))
