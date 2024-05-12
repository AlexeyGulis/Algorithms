from heapq import heapify
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify(sorted(stones))
        if stones:
            while True:
                if len(stones) == 1:
                    return stones[0]
                else:
                    t1 = -1
                    index1 = 0
                    for i in range(len(stones)):
                        if t1 < stones[i]:
                            t1 = stones[i]
                            index1 = i
                    stones[index1] = stones[-1]
                    stones.pop()
                    t2 = -1
                    index1 = 0
                    for i in range(len(stones)):
                        if t2 < stones[i]:
                            t2 = stones[i]
                            index1 = i
                    stones[index1] = stones[-1]
                    stones.pop()
                    if t1 - t2 != 0:
                        stones.append(t1 - t2)
                    else:
                        if not stones:
                            stones.append(t1 - t2)
                    heapify(stones)
        else:
            return 0


s = Solution()

print(s.lastStoneWeight([2,7,4,1,8,1]))
