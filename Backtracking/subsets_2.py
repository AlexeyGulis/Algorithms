from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        self.rec_help(nums, 0, answer, [])
        return answer

    def rec_help(self, nums, i, answer, temp):
        if i >= len(nums):
            answer.append(temp)
            return
        if not temp:
            new_temp = [nums[i]]
        else:
            new_temp = list(temp)
            new_temp.append(nums[i])
        self.rec_help(nums, i + 1, answer, new_temp)
        if i + 1 >= len(nums):
            answer.append(temp)
            return
        j = i + 1
        while True:
            if j >= len(nums):
                answer.append(temp)
                return
            if nums[j] != nums[i]:
                break
            j += 1
        self.rec_help(nums, j, answer, temp)


s = Solution()
print(s.subsetsWithDup([1, 2, 2, 3]))
