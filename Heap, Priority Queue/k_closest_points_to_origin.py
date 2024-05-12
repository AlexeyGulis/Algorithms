from heapq import heapify, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        my_dict = {}
        for lv in points:
            dist = lv[0] * lv[0] + lv[1] * lv[1]
            heap.append(dist)
            if dist in my_dict:
                my_dict[dist].append(lv)
            else:
                my_dict[dist] = [lv]
        heapify(heap)
        answer = []
        for i in range(k):
            answer.append(my_dict[heap[0]].pop())
            heappop(heap)
        return answer


s = Solution()
print(s.kClosest(points =
[[0,1],[1,0]], k = 2))
