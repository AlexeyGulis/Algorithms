from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_edge = {}
        answer = 0

        def dfs(queue):
            if not queue:
                return
            temp = []
            while queue:
                node = queue.pop()
                if node in node_edge:
                    for node_e in node_edge[node]:
                        del node_edge[node_e][node_edge[node_e].index(node)]
                        temp.append(node_e)
                    del node_edge[node]
            dfs(temp)

        for i in range(n):
            node_edge[i] = []
        for i in range(len(edges)):
            node_edge[edges[i][0]].append(edges[i][1])
            node_edge[edges[i][1]].append(edges[i][0])

        for i in range(n):
            if i in node_edge:
                answer += 1
                dfs([i])
        return answer


s = Solution()
print(s.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]))
