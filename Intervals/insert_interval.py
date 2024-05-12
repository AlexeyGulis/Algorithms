from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        cur = [newInterval[0], newInterval[1]]
        pointer = True
        for interval in intervals:

            if cur[0] > interval[1]:
                answer.append(interval)
                continue
            if cur[1] < interval[0]:
                if pointer:
                    answer.append(cur)
                    answer.append(interval)
                    pointer = False
                    continue
                if not pointer:
                    answer.append(interval)
                continue
            if cur[0] <= interval[0] and cur[1] >= interval[1]:
                cur = [cur[0], cur[1]]
                continue
            if cur[0] > interval[0] and cur[1] >= interval[1]:
                cur = [interval[0], cur[1]]
                continue
            if cur[0] > interval[0] and cur[1] < interval[1]:
                cur = [interval[0], interval[1]]
                continue
            if cur[0] <= interval[0] and cur[1] < interval[1]:
                cur = [cur[0], interval[1]]
        if pointer:
            answer.append(cur)
        return answer


s = Solution()
print(s.insert(intervals =
[[2,5],[6,7],[8,9]], newInterval = [0,1]))

