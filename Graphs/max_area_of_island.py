from typing import List


class Solution:
    max_area = 0
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0])
        double_grid = [[0 for x in range(w)] for y in range(h)]
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and double_grid[i][j] != 1:
                    self.max_area = 0
                    self.help_rec(grid, double_grid, i, j)
                    answer = max(self.max_area, answer)
        return answer

    def help_rec(self, grid, double_grid, i, j):
        double_grid[i][j] = 1
        self.max_area += 1
        if j + 1 < len(grid[i]) and grid[i][j + 1] != 0 and double_grid[i][j + 1] != 1:
            self.help_rec(grid, double_grid, i, j + 1)

        if j - 1 >= 0 and grid[i][j - 1] != 0 and double_grid[i][j - 1] != 1:
            self.help_rec(grid, double_grid, i, j - 1)

        if i + 1 < len(grid) and grid[i + 1][j] != 0 and double_grid[i + 1][j] != 1:
            self.help_rec(grid, double_grid, i + 1, j)

        if i - 1 >= 0 and grid[i - 1][j] != 0 and double_grid[i - 1][j] != 1:
            self.help_rec(grid, double_grid, i - 1, j)


s = Solution()
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))