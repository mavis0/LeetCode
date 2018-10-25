# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        res = list()
        if not intervals: return intervals
        s, e = intervals[0].start, intervals[0].end
        for i in intervals[1: ]:
            if i.start <= e:
                e = max(i.end, e)
            else:
                res.append(Interval(s, e))
                s, e = i.start, i.end

        res.append(Interval(s, e))
        return res
s = Solution()
i = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
for k in s.merge(i):
    print(k, end=',')


