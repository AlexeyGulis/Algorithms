from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        nodes = [i + 1 for i in range(n)]
        size = [1 for i in range(n)]

        def find(i):
            while nodes[i - 1] != i:
                nodes[i - 1] = nodes[nodes[i - 1] - 1]
                i = nodes[i - 1]
            return i

        def union_nodes(i, j):
            if size[i - 1] < size[j - 1]:
                nodes[i - 1] = nodes[j - 1]
                size[j - 1] += size[i - 1]
            else:
                if nodes[i - 1] < nodes[j - 1]:
                    nodes[j - 1] = nodes[i - 1]
                    size[i - 1] += size[j - 1]
                else:
                    nodes[i - 1] = nodes[j - 1]
                    size[j - 1] += size[i - 1]

        for i in range(n):
            x = find(edges[i][0])
            y = find(edges[i][1])
            if x == y:
                return edges[i]
            union_nodes(x, y)
        return []


s = Solution()
print(s.findRedundantConnection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]))
