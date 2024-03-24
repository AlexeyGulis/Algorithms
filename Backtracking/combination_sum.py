from typing import List


class Solution:
    answer = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.answer = []
        candidates = sorted(candidates)

        for i in range(len(candidates)):
            self.recursion_help(candidates[i], i, [candidates[i]], target, candidates)
        return self.answer

    def recursion_help(self, my_sum, left, my_l, target, candidates):
        if left == len(candidates):
            return
        if my_sum == target:
            self.answer.append(list(my_l))
            return
        if my_sum > target:
            return
        if my_sum + candidates[left] > target:
            return
        my_temp = list(my_l)
        my_temp.append(candidates[left])
        self.recursion_help(my_sum + candidates[left], left, my_temp, target, candidates)
        self.recursion_help(my_sum, left + 1, my_l, target, candidates)



s = Solution()
print(s.combinationSum(candidates = [7,3,2], target = 18))
