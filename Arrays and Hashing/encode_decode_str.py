from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs)):
            ans = ans + 'DelimiterForString.' + strs[i]
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        if s == '':
            return ans
        else:
            t = s.split('DelimiterForString.')
            for i in range(1, len(t)):
                ans.append(t[i])
            return ans


s = Solution()

print(len([""]))

print(s.decode(s.encode(["we", "say", ":", "yes"])))
