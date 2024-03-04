from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = {}

        for num in nums:
            my_dict[num] = 0

        my_dict = sorted(my_dict)
        prev_num = None
        max_l = 0
        long = 0
        for k in my_dict:

            if prev_num is None:
                prev_num = k
                long = 1
            else:
                if k == prev_num + 1:
                    long += 1
                    prev_num = k
                else:
                    if long > max_l:
                        max_l = long
                    long = 1
                    prev_num = k

        if long > max_l:
            max_l = long
        return max_l


s = Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))