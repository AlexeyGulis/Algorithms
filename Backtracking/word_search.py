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
                    my_dict = {}
                    my_dict[i] = [j]
                    self.rec_help(board, word, i, j, 1, word[0], my_dict)
        return self.answer

    def rec_help(self, board, word, i, j, k, my_word, my_dict):
        if my_word == word:
            self.answer = True
            return
        if self.answer:
            return
        if j + 1 < len(board[i]) and board[i][j + 1] == word[k]:
            if i in my_dict:
                if j + 1 not in my_dict[i]:
                    temp_dict = copy.deepcopy(my_dict)
                    temp_dict[i].append(j + 1)
                    temp = my_word + word[k]
                    self.rec_help(board, word, i, j + 1, k + 1, temp, temp_dict)
            else:
                temp_dict = copy.deepcopy(my_dict)
                temp_dict[i] = [j + 1]
                temp = my_word + word[k]
                self.rec_help(board, word, i, j + 1, k + 1, temp, temp_dict)
        if j - 1 >= 0 and board[i][j - 1] == word[k]:
            if i in my_dict:
                if j - 1 not in my_dict[i]:
                    temp_dict = copy.deepcopy(my_dict)
                    temp_dict[i].append(j - 1)
                    temp = my_word + word[k]
                    self.rec_help(board, word, i, j - 1, k + 1, temp, temp_dict)
            else:
                temp_dict = copy.deepcopy(my_dict)
                temp_dict[i] = [j - 1]
                temp = my_word + word[k]
                self.rec_help(board, word, i, j - 1, k + 1, temp, temp_dict)
        if i + 1 < len(board) and board[i + 1][j] == word[k]:
            if i + 1 in my_dict:
                if j not in my_dict[i + 1]:
                    temp_dict = copy.deepcopy(my_dict)
                    temp_dict[i + 1].append(j)
                    temp = my_word + word[k]
                    self.rec_help(board, word, i + 1, j, k + 1, temp, temp_dict)
            else:
                temp_dict = copy.deepcopy(my_dict)
                temp_dict[i + 1] = [j]
                temp = my_word + word[k]
                self.rec_help(board, word, i + 1, j, k + 1, temp, temp_dict)
        if i - 1 >= 0 and board[i - 1][j] == word[k]:
            if i - 1 in my_dict:
                if j not in my_dict[i - 1]:
                    temp_dict = copy.deepcopy(my_dict)
                    temp_dict[i - 1].append(j)
                    temp = my_word + word[k]
                    self.rec_help(board, word, i - 1, j, k + 1, temp, temp_dict)
            else:
                temp_dict = copy.deepcopy(my_dict)
                temp_dict[i - 1] = [j]
                temp = my_word + word[k]
                self.rec_help(board, word, i - 1, j, k + 1, temp, temp_dict)


s = Solution()
print(s.exist([["A","B","C"],["H","G","D"],["I","F","E"]], "ABCDEFGHI"))
