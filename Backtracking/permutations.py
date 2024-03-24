from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums)):
            self.recur_help(list(nums[0:i] + nums[i + 1:]), [nums[i]], answer)
        return answer

    def recur_help(self, my_list, my_temp, answer):
        if len(my_list) == 0:
            answer.append(list(my_temp))
        for i in range(len(my_list)):
            temp = list(my_temp)
            temp.append(my_list[i])
            self.recur_help(my_list[0:i] + my_list[i + 1:], temp, answer)




s = Solution()
print(s.permute([1,2,3]))
