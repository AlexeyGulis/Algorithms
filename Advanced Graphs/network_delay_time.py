import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append([w, v])
        ans = 0
        visit = set()
        minHeap = [[0, k]]
        max_time = 0
        while len(visit) < n:
            if minHeap:
                time, node = heapq.heappop(minHeap)
                if node in visit:
                    continue
                visit.add(node)
                if max_time < time:
                    max_time = time
                for time_nei, nei in adj[node]:
                    if nei not in visit:
                        heapq.heappush(minHeap, [time_nei + time, nei])

            else:
                return -1
        return max_time


s = Solution()
print(s.networkDelayTime(times = [[1,2,1],[2,3,2],[1,3,4]], n = 3, k = 1))
