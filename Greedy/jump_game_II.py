from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        my_array = [0 for i in range(len(nums))]
        i = 0
        j = 0
        max_next = 0
        res = 0
        while i < len(nums):
            my_array[i] = res
            if i == 0:
                j = nums[0]
                i += 1
                res += 1
                continue
            if i + nums[i] > max_next:
                max_next = i + nums[i]
            if j == i:
                j = max_next
                res += 1
            i += 1

        return my_array[len(my_array) - 1]


s = Solution()
print(s.jump(nums =
[7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))

