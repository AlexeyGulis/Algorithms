from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates = sorted(candidates)
        self.recur_help(0, 0, [], target, candidates, answer)
        return answer

    def recur_help(self, my_sum, i, my_l, target, candidates, answer):
        if my_sum == target:
            answer.append(my_l)
            return
        if i == len(candidates):
            return
        if my_sum > target:
            return
        if my_sum + candidates[i] > target:
            return

        temp = list(my_l)
        temp.append(candidates[i])
        self.recur_help(my_sum + candidates[i], i + 1, temp, target, candidates, answer)
        j = i + 1
        while True:
            if j >= len(candidates):
                return
            if candidates[j] != candidates[i]:
                break
            j += 1
        self.recur_help(my_sum, j, my_l, target, candidates, answer)


s = Solution()
print(s.combinationSum2(candidates = [2,5,2,1,2], target = 5))
