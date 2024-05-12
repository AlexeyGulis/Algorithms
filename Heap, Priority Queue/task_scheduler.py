from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        my_dict = {}
        for i in range(len(tasks)):
            if tasks[i] in my_dict:
                my_dict[tasks[i]] -= 1
            else:
                my_dict[tasks[i]] = -1
        j = 1
        heap = list(my_dict.values())
        heapify(heap)
        print(heap)
        my_queue = []
        while True:
            if my_queue:
                if my_queue[0][1] <= j:
                    t = my_queue.pop(0)
                    heappush(heap, t[0])
            if heap:
                st = heappop(heap)
                st += 1
                if st != 0:
                    my_queue.append([st, j + n + 1])
            if not heap and not my_queue:
                break
            j += 1
        return j


s = Solution()
print(s.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G","G"], n = 1))
