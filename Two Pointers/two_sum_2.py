from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     if numbers[i] + numbers[len(numbers) - 1] < target:
        #         continue
        #     j = i + 1
        #     while numbers[i] + numbers[j] <= target:
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        #         j += 1
        my_dict = {}
        for i in range(len(numbers)):
            my_dict[numbers[i]] = i
        for i in range(len(numbers)):
            if target - numbers[i] in my_dict:
                return [i + 1, my_dict[target - numbers[i]] + 1]

        return []


s = Solution()
print(s.twoSum(numbers=[-1, 0], target=-1))
