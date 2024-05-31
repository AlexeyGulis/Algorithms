from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        i = 0
        while True:
            if n - i - 1 <= 1:
                break
            for j in range(i, n - i - 1):
                temp1 = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[i][j]
                temp2 = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = temp1
                temp1 = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = temp2
                matrix[i][j] = temp1
            i += 1


s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
s.rotate(matrix)
print(matrix)
