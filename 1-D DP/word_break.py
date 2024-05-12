from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = []
        for i in range(len(s)):
            for j in range(len(dp)):
                if s[dp[j] + 1:i + 1] in wordDict:
                    dp.append(i)
                    break
            if s[0:i+1] in wordDict:
                dp.append(i)
        return True if len(dp) != 0 and dp[len(dp) - 1] == len(s) - 1 else False


s = Solution()
print(s.wordBreak(s = "a", wordDict = ["b"]))
