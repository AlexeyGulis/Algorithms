from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        my_dict = {}
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            my_dict[nums[i]] = i
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            j = i + 1
            while j < len(nums) - 1:
                req = 0 - nums[i] - nums[j]
                if req in my_dict and my_dict[req] > j:
                    val = my_dict[req]
                    if i != val and j != val:
                        ans.append([nums[i], nums[j], req])
                j = my_dict[nums[j]] + 1
            i = my_dict[nums[i]] + 1

        return ans


s = Solution()
print(s.threeSum(
    nums=
    [-1, 0, 1, 2, -1, -4]
))
