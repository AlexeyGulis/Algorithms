from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(amount + 1)] for i in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                dp[i][j] = 0
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j - coins[i]]
                if i < len(coins) - 1:
                    dp[i][j] += dp[i + 1][j]
        return dp[0][amount]


s = Solution()
print(s.change(6, [1, 2, 5]))
