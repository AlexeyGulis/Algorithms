from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        my_array = []
        for num in nums:
            if my_array:
                temp = my_array[len(my_array) - 1]
                if temp + num > num:
                    my_array.append(temp + num)
                else:
                    my_array.append(num)
            else:
                my_array.append(num)
        print(my_array)
        return max(my_array)


s = Solution()
print(s.maxSubArray(nums = [1]))
