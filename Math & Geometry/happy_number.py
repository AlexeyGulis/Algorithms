class Solution:
    def isHappy(self, n: int) -> bool:
        list_numbers = []
        while True:
            if n in list_numbers:
                return False
            else:
                list_numbers.append(n)
            if n == 1:
                return True
            n_str = str(n)
            n = 0
            for s in n_str:
                n += int(s) ** 2


s = Solution()
print(s.isHappy(19))
