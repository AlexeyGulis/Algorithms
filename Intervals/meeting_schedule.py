from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        cur = []
        for interval in intervals:
            if cur:
                if cur.end > interval.start:
                    return False
                else:
                    cur = interval
            else:
                cur = interval
        return True


s = Solution()

print(s.canAttendMeetings(intervals = [Interval(0,30),Interval(5,10),Interval(15,20)]))
