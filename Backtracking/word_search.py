import copy
from typing import List


class Solution:
    answer = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.answer = False
        my_dict_board = {}
        my_dict_word = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in my_dict_board:
                    my_dict_board[board[i][j]] += 1
                else:
                    my_dict_board[board[i][j]] = 1
        for i in range(len(word)):
            if word[i] in my_dict_board:
                if word[i] in my_dict_word:
                    my_dict_word[word[i]] += 1
                    if my_dict_board[word[i]] < my_dict_word[word[i]]:
                        return self.answer
                else:
                    my_dict_word[word[i]] = 1
            else:
                return self.answer
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.answer:
                    break
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = ''
                    self.rec_help(board, word, i, j, 1, word[0])
                    board[i][j] = temp
        return self.answer

    def rec_help(self, board, word, i, j, k, my_word):
        if my_word == word:
            self.answer = True
            return
        if self.answer:
            return
        if j + 1 < len(board[i]) and board[i][j + 1] == word[k]:
            new_board = copy.deepcopy(board)
            new_board[i][j + 1] = ''
            temp = my_word + word[k]
            self.rec_help(new_board, word, i, j + 1, k + 1, temp)
        if j - 1 >= 0 and board[i][j - 1] == word[k]:
            new_board = copy.deepcopy(board)
            new_board[i][j - 1] = ''
            temp = my_word + word[k]
            self.rec_help(new_board, word, i, j - 1, k + 1, temp)
        if i + 1 < len(board) and board[i + 1][j] == word[k]:
            new_board = copy.deepcopy(board)
            new_board[i + 1][j] = ''
            temp = my_word + word[k]
            self.rec_help(new_board, word, i + 1, j, k + 1, temp)
        if i - 1 >= 0 and board[i - 1][j] == word[k]:
            new_board = copy.deepcopy(board)
            new_board[i - 1][j] = ''
            temp = my_word + word[k]
            self.rec_help(new_board, word, i - 1, j, k + 1, temp)


s = Solution()
print(s.exist([["A"],["A"],["A"],["A"],["A"],["A"]], word =
"AAAAAAAAAAAAAAB"))
