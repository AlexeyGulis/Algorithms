from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        my_sum = [cost[0], cost[1]]
        i = 2
        while i < len(cost):
            a1 = cost[i]
            if i + 1 >= len(cost):
                a2 = 0
            else:
                a2 = cost[i + 1]
            my_sum.append(min(cost[i] + my_sum[len(my_sum) - 1], cost[i] + my_sum[len(my_sum) - 2]))
            i += 1
        my_sum.append(min(my_sum[len(my_sum) - 1], my_sum[len(my_sum) - 2]))
        return my_sum[len(my_sum) - 1]

s = Solution()
print(s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
