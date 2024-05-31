from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        my_list_i = []
        my_list_j = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in my_list_i:
                        my_list_i.append(i)
                    if j not in my_list_j:
                        my_list_j.append(j)
        while my_list_i:
            i = my_list_i.pop()
            for t in range(len(matrix[0])):
                matrix[i][t] = 0
        while my_list_j:
            j = my_list_j.pop()
            for t in range(len(matrix)):
                matrix[t][j] = 0



s = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(matrix)
s.setZeroes(matrix)
print(matrix)
