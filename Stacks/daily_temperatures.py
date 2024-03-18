from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = list(range(len(temperatures)))
        my_stack = list()
        for i in range(len(temperatures) - 1):
            if temperatures[i + 1] > temperatures[i]:
                answer[i] = 1
                while len(my_stack) > 0:
                    if temperatures[i + 1] > list(my_stack[len(my_stack) - 1].keys())[0]:
                        v = list(my_stack.pop().values())[0]
                        answer[v] = i + 1 - v
                    else:
                        break
            else:
                my_stack.append({temperatures[i]: i})
        answer[len(answer) - 1] = 0
        while len(my_stack) > 0:
            v = list(my_stack.pop().values())[0]
            answer[v] = 0

        return answer


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
