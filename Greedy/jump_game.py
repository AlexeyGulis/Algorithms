from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        my_array = [0 for i in range(len(nums))]

        i = 0
        j = 1
        while i < len(nums):
            if j != 0:
                my_array[i] = 1
                j -= 1
            if nums[i] > j:
                j = nums[i]

            i += 1

        print(my_array)

        return my_array[len(my_array) - 1] == 1 and my_array[0] == 1


s = Solution()
print(s.canJump(nums = [2,3,1,1,4]))
