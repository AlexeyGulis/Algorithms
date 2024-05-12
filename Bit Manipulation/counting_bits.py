from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        r = 2
        for i in range(1, n + 1):
            if i % 2 != 0:
                res.append(res[len(res) - 1] + 1)
            else:
                if i == r:
                    res.append(1)
                    r *= 2
                else:
                    res.append(res[i // 2])
        return res


s = Solution()
print(s.countBits(15))