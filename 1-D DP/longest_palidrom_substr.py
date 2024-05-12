class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        my_s = ''

        for i in range(len(s)):
            left = i
            right = i
            while True:
                if left < 0:
                    break
                if right == len(s):
                    break
                if s[left] == s[right]:
                    if (right - left) + 1 > max_len:
                        my_s = s[left:right + 1]
                        max_len = (right - left) + 1
                else:
                    break
                left -= 1
                right += 1
            left, right = i, i + 1
            while True:
                if left < 0:
                    break
                if right == len(s):
                    break
                if s[left] == s[right]:
                    if (right - left) + 1 > max_len:
                        my_s = s[left:right + 1]
                        max_len = (right - left) + 1
                else:
                    break
                left -= 1
                right += 1
        return my_s


s = Solution()
print(s.longestPalindrome('bb'))