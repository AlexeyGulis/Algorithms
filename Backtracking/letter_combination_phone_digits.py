from typing import List


class Solution:
    num_letter_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        self.help_rec('', 0, 0, digits, answer)
        return answer

    def help_rec(self, temp, i, j, digits, answer):
        if i == len(digits):
            answer.append(temp)
            return
        if j == len(self.num_letter_dict[digits[i]]):
            return
        my_str = '' + temp
        my_str = my_str + self.num_letter_dict[digits[i]][j]
        self.help_rec(my_str, i + 1, 0, digits, answer)
        self.help_rec(temp, i, j + 1, digits, answer)


s = Solution()
print(s.letterCombinations('23'))
