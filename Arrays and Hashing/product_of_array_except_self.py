from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_array = len(nums)
        array_a = list(range(length_array))
        array_b = list(range(length_array))
        ans = []
        array_a[0] = nums[0]
        array_b[length_array - 1] = nums[length_array - 1]
        for i in range(1, length_array):
            array_a[i] = array_a[i - 1] * nums[i]
        for i in reversed(range(length_array - 1)):
            array_b[i] = array_b[i + 1] * nums[i]

        for i in range(length_array):
            if i == 0:
                ans.append(array_b[i + 1])
            elif i == length_array - 1:
                ans.append(array_a[i - 1])
            else:
                ans.append(array_a[i - 1] * array_b[i + 1])
        return ans


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
