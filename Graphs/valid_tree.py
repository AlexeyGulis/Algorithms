from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = [i for i in range(n)]
        size = [1 for i in range(n)]

        def find(i):
            while nodes[i] != i:
                nodes[i] = nodes[nodes[i]]
                i = nodes[i]
            return i

        def union_nodes(i, j):
            if size[i] < size[j]:
                nodes[i] = nodes[j]
                size[j] += size[i]
            else:
                if nodes[i] < nodes[j]:
                    nodes[j] = nodes[i]
                    size[i] += size[j]
                else:
                    nodes[i] = nodes[j]
                    size[j] += size[i]

        for i in range(len(edges)):
            x = find(edges[i][0])
            y = find(edges[i][1])
            if x == y:
                return False
            union_nodes(x, y)
        for i in range(1, n):
            x = find(nodes[i])
            y = find(nodes[i - 1])
            if x != y:
                return False
        return True


s = Solution()
print(s.validTree(n=4
,edges=[[0,1],[2,3]]))
