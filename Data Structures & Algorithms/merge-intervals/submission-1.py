class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            s1 = ans[-1][0]
            f1 = ans[-1][1]

            s2 = intervals[i][0]
            f2 = intervals[i][1]

            if s2 <= f1:
                ans[-1] = ([min(s1,s2),max(f1,f2)])
            else:
                ans.append([s2,f2])
        return ans