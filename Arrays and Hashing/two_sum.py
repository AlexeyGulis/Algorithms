from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in my_dict:
                if target - nums[i] != nums[i]:
                    return [i, my_dict[target - nums[i]]]
                else:
                    if my_dict[target - nums[i]] != i:
                        return [i, my_dict[target - nums[i]]]
        return []


s = Solution()

print(s.twoSum(nums = [2,7,11,15], target = 9))

