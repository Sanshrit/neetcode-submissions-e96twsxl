"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = [(x.start,x.end) for x in intervals]
        intervals.sort()
        for i in range(0,len(intervals)-1):
            f1 = intervals[i][1]
            s2 = intervals[i+1][0]
            if s2 < f1:
                return False
        return True