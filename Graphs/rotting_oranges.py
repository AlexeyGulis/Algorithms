from typing import List


class Solution:
    answer = 0
    minutes = 0
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.answer = 0
        ROW, COL = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def check_neighbor(row, col, grid):
            if row < 0 or row == ROW:
                return False
            if col < 0 or col == COL:
                return False
            if grid[row][col] != 1:
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
                    if check_neighbor(n_row + drow, n_col + dcol, grid):
                        temp.append([n_row + drow, n_col + dcol])
                        grid[n_row + drow][n_col + dcol] = 3
                        my_p = True   
            if my_p:
                self.answer += 1
            dfs(grid, temp)


        my_queue = []
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    my_queue.append((i, j))
        dfs(grid, my_queue)
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1
        return self.answer


s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))
