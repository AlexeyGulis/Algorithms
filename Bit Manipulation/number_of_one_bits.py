class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            if n % 2 != 0:
                res += 1
            n = n >> 1
        return res


s = Solution()
print(s.hammingWeight(n = 2147483645))
