from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        my_list = []
        self.recurs_tree(n, n, my_list, '')
        return my_list

    def recurs_tree(self, n, m, my_list, str):
        if n > 0:
            first_str = str + '('
            self.recurs_tree(n - 1, m, my_list, first_str)
        if n >= m and n != 0:
            return
        if m > 0:
            second_str = str + ')'
            self.recurs_tree(n, m - 1, my_list, second_str)
            # str += ')'
            # self.recurs_tree(n, m - 1, my_list, str)
        if n == 0 and m == 0:
            my_list.append(str)


s = Solution()
print(s.generateParenthesis(3))
