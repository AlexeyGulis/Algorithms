class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        remind = 0
        carry = 1
        c1 = a
        c2 = b
        for i in range(32):
            t1 = 0
            t2 = 0
            if c1 % 2 != 0:
                t1 = 1
            if c2 % 2 != 0:
                t2 = 1
            if (t1 ^ t2) ^ remind:
                res = res | carry
            if remind:
                remind = t1 | t2
            else:
                remind = t1 & t2
            c1 = c1 >> 1
            c2 = c2 >> 1
            carry = carry << 1
        mask = 0xFFFFFFFF
        if a < 0:
            if b > 0:
                if abs(a) > b:
                    return ~(res ^ mask)
        if b < 0:
            if a > 0:
                if abs(b) > a:
                    return ~(res ^ mask)
        if a < 0 and b < 0:
            return ~(res ^ mask)
        return res


s = Solution()
print(s.getSum(6, -4))
