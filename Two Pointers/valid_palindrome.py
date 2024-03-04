import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[\W_]+', '', s)
        print(s)
        j = len(s) - 1
        for i in range(len(s) // 2):
            if s[i] != s[j]:
                return False
            j -= 1
        return True


s = Solution()
print(s.isPalindrome("ab_a"))
