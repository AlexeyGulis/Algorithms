from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        res, count_days = 0, 0
        i, j = 0, 0
        while i < len(start):
            if start[i] < end[j]:
                count_days += 1
                i += 1
            else:
                count_days -= 1
                j += 1
            res = max(count_days, res)
        return res


s = Solution()

print(s.minMeetingRooms(intervals=[Interval(1,5),Interval(5,10),Interval(10,15),Interval(15,20),Interval(1,20),Interval(2,6)]))
