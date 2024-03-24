from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        answer.append([])
        prev = []
        for i in range(len(nums)):

            answer.append(list([nums[i]]))
            prev.append(list([nums[i]]))
            for j in range(len(prev) - 1):
                temp1 = list(prev[j])
                temp1.append(nums[i])
                answer.append(list(temp1))
                prev.append(temp1)
        return answer


s = Solution()
print(s.subsets([1,2,2]))
