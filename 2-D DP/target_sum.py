from typing import List


class Solution:
    result = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Brute Force Dec Tree Solution

        # self.result = 0
        #
        # def decisionTree(i, sum):
        #     if i >= len(nums):
        #         if sum == target:
        #             self.result += 1
        #         return
        #     decisionTree(i + 1, sum + nums[i])
        #     decisionTree(i + 1, sum - nums[i])
        #
        # decisionTree(0, 0)

        # DP solution
        dp = {}

        def backtracking(i, curr):
            if i == len(nums):
                return 1 if curr == target else 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            dp[(i, curr)] = backtracking(i + 1, curr + nums[i]) + backtracking(i + 1, curr - nums[i])
            return dp[(i, curr)]

        return backtracking(0, 0)


s = Solution()
print(s.findTargetSumWays([49, 19, 9, 12, 16, 21, 7, 5, 32, 50, 31, 40, 14, 15, 1, 8, 33, 5, 9, 26], 12))
