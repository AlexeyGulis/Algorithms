class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        two_d_array = [[0 for i in range(n)] for i in range(m)]
        two_d_array[0][0] = 1
        for i in range(m):
            for j in range(n):
                if j != 0:
                    two_d_array[i][j] += two_d_array[i][j - 1]
                if i != 0:
                    two_d_array[i][j] += two_d_array[i - 1][j]
        return two_d_array[m - 1][n - 1]


s = Solution()
print(s.uniquePaths(3, 7))
