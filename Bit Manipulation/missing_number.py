import math
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # res = None
        # for n in nums:
        #     if res is None:
        #         res = n
        #     else:
        #         res = XNOR(res, n)
        #         print(res)

        a = 9
        b = 6
        leftshift = int(math.log(max(a, b), 2))
        r = ~(a ^ b)
        print(bin(r))
        return 0


s = Solution()
print(s.missingNumber(nums=[3, 0, 1]))
