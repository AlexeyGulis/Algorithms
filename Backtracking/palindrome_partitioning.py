from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        temp = []
        for i in range(len(s)):
            temp.append(s[i])
        self.help_rec(temp, 0, answer)
        return answer

    def help_rec(self, temp, index, answer):
        if index == len(temp) - 1:
            for ms in temp:
                if not self.isPalindrome(ms):
                    return
            answer.append(temp)
            return
        my_temp = []
        my_t = ''
        for i in range(len(temp)):
            if index <= i <= index + 1:
                my_t += temp[i]
                if i == index + 1:
                    my_temp.append(my_t)
            else:
                my_temp.append(temp[i])

        self.help_rec(my_temp, index, answer)

        self.help_rec(temp, index + 1, answer)

    def isPalindrome(self, s):
        return s == s[::-1]


s = Solution()
print(s.partition('abbab'))
