from typing import List


class Solution:
    answer = 0

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {coins[i]: 1 for i in range(len(coins))}
        coins.sort()
        for i in range(amount + 1):
            if i in dp:
                continue
            dp[i] = 0
            for j in range(len(coins)):
                if i - coins[j] > 0:
                    if dp[i - coins[j]] != 0:
                        if dp[i] == 0:
                            dp[i] = dp[i - coins[j]] + 1
                        else:
                            dp[i] = dp[i] if dp[i - coins[j]] + 1 > dp[i] else dp[i - coins[j]] + 1
                else:
                    break

        return dp[amount] if dp[amount] != 0 else -1


s = Solution()
print(s.coinChange(coins=[474, 83, 404, 3], amount=264))
