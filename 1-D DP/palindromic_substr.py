class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            left = i
            right = i
            while True:
                if left < 0:
                    break
                if right == len(s):
                    break
                if s[left] == s[right]:
                    ans += 1
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
                    ans += 1
                else:
                    break
                left -= 1
                right += 1
        return ans


s = Solution()
print(s.countSubstrings(s = "abc"))
