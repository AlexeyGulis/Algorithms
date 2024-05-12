class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        my_str = ''.join(reversed(str(n)))
        j = 31
        for i in range(len(my_str)):
            if my_str[i] == '1':
                res += pow(2, j)
            j -= 1
        return res


s = Solution()
print(s.reverseBits(n = 11111111111111111111111111111101))
