from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        my_array = [gas[i] - cost[i] for i in range(n)]
        if sum(my_array) < 0:
            return -1
        my_sum = 0
        index = -1
        for i in range(n):
            if my_array[i] + my_sum < 0:
                my_sum = 0
                index = -1
            else:
                if index == -1:
                    index = i
                my_sum += my_array[i]
        return index


s = Solution()
print(s.canCompleteCircuit(gas =
[2,0,1,2,3,4,0], cost =
[0,1,0,0,0,0,11]))
