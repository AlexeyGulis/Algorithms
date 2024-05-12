from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647

        def check_neighbor(row, col, grid, val):
            if row < 0 or row == ROW:
                return False
            if col < 0 or col == COL:
                return False
            if grid[row][col] == -1:
                return False
            if grid[row][col] != 2147483647:
                if grid[row][col] < val:
                    return False
            return True

        def dfs(grid, queue):
            if not queue:
                return
            temp = []
            my_p = False
            while queue:
                n_row, n_col = queue.pop()
                for drow, dcol in DIRECTIONS:
                    if check_neighbor(n_row + drow, n_col + dcol, grid, grid[n_row][n_col] + 1):
                        temp.append([n_row + drow, n_col + dcol])
                        grid[n_row + drow][n_col + dcol] = grid[n_row][n_col] + 1
            dfs(grid, temp)

        my_queue = []

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    my_queue.append((i, j))

        dfs(grid, my_queue)


s = Solution()
grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
s.islandsAndTreasure(grid)
print(grid)
