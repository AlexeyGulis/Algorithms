from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = None
        for num in prices:
            if min is None:
                min = num
            else:
                if num < min:
                    min = num
                if num > min:
                    if profit == 0:
                        profit = num - min
                    elif profit < num - min:
                        profit = num - min

        return profit


s = Solution()
print(s.maxProfit([7,6,4,3,1]))
