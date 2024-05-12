from typing import List
from operator import itemgetter


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        cur = []
        intervals.sort(key=itemgetter(0))
        for interval in intervals:
            if not cur:
                cur = interval
            else:
                if interval[0] > cur[1]:
                    res.append(cur)
                    cur = interval
                    continue
                if interval[1] < cur[0]:
                    res.append(interval)
                    continue
                if interval[0] <= cur[0] and interval[1] >= cur[1]:
                    cur = [interval[0], interval[1]]
                    continue
                if interval[0] > cur[0] and interval[1] >= cur[1]:
                    cur = [cur[0], interval[1]]
                    continue
                if interval[0] <= cur[0] and interval[1] < cur[1]:
                    cur = [interval[0], cur[1]]
                    continue
                if interval[0] > cur[0] and interval[1] < cur[1]:
                    cur = [cur[0], cur[1]]
                    continue
        res.append(cur)
        return res


s = Solution()
print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
