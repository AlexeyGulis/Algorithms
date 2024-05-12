import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        answer = 0

        V = len(points)

        adj = {i: [] for i in range(V)}
        for i in range(V):
            for j in range(i + 1, V):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        visit = set()
        minHeap = [[0, 0]]

        while len(visit) < V:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            answer += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [nei_cost, nei])

        return answer


s = Solution()
print(s.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
