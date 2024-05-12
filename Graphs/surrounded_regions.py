import queue
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        ROW, COL = len(board), len(board[0])

        def bfs(row, col, que):
            if row == ROW or row < 0:
                return
            if col == COL or col < 0:
                return
            if board[row][col] == 'X' or board[row][col] == '1':
                return
            que.put((row, col))
            board[row][col] = '1'
            while not que.empty():
                q_row, q_col = que.get()
                for dROW, dCOL in DIRECTIONS:
                    bfs(q_row + dROW, q_col + dCOL, que)

        for i in range(ROW):
            if board[i][0] == 'O':
                bfs(i, 0, queue.Queue())
            if board[i][COL - 1] == 'O':
                bfs(i, COL - 1, queue.Queue())
        for i in range(COL):
            if board[0][i] == 'O':
                bfs(0, i, queue.Queue())
            if board[ROW - 1][i] == 'O':
                bfs(ROW - 1, i, queue.Queue())

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


        """
        Do not return anything, modify board in-place instead.
        """


s = Solution()
s.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])

s = 0
