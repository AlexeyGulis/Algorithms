from typing import List
from operator import itemgetter


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals_copy = []
        intervals.sort(key=itemgetter(0))
        cur = []
        for interval in intervals:
            if cur:
                if cur[1] > interval[0]:
                    if cur[1] > interval[1]:
                        cur = interval
                else:
                    intervals_copy.append(cur)
                    cur = interval
            else:
                cur = interval
        intervals_copy.append(cur)
        return len(intervals) - len(intervals_copy)


s = Solution()
print(s.eraseOverlapIntervals([[2,3],[4,5],[6,7],[8,9],[1,10]]))
