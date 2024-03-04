from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_dicts_columns = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        list_dicts_cells = [[{}, {}, {}],
                            [{}, {}, {}],
                            [{}, {}, {}]]
        for i in range(len(board)):
            dict_row = {}
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in dict_row:
                        return False
                    else:
                        dict_row[board[i][j]] = True
                    if board[i][j] in list_dicts_columns[j]:
                        return False
                    else:
                        list_dicts_columns[j][board[i][j]] = True
                    if board[i][j] in list_dicts_cells[i // 3][j // 3]:
                        return False
                    else:
                        list_dicts_cells[i // 3][j // 3][board[i][j]] = True

        return True


s = Solution()
print(s.isValidSudoku(board=
                      [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
