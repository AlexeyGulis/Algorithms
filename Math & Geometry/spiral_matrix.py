from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        pointer_axis = True
        pointer_i, pointer_j = True, True
        count = 0
        i, j = 0, 0
        left_i, right_i = 0, m
        left_j, right_j = 0, n
        while count < m * n:
            if pointer_axis:
                pointer_axis = False
                if pointer_j:
                    for k in range(left_j, right_j):
                        res.append(matrix[i][k])
                        count += 1
                    left_i += 1
                    j = right_j - 1
                    pointer_j = False
                else:
                    for k in range(right_j - 1, left_j - 1, - 1):
                        res.append(matrix[i][k])
                        count += 1
                    right_i -= 1
                    j = left_j
                    pointer_j = True
            else:
                pointer_axis = True
                if pointer_i:
                    for k in range(left_i, right_i):
                        res.append(matrix[k][j])
                        count += 1
                    right_j -= 1
                    i = right_i - 1
                    pointer_i = False
                else:
                    for k in range(right_i - 1, left_i - 1, - 1):
                        res.append(matrix[k][j])
                        count += 1
                    left_j += 1
                    i = left_i
                    pointer_i = True
        return res


s = Solution()
print(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
