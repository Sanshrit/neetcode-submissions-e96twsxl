class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = [intervals[0]]
        for st,en in intervals[1:]:
            s1 = ans[-1][0]
            f1 = ans[-1][1]
            s2 = st
            f2 = en
            if f1 >= s2:
                ans[-1][1] = max(f1,f2)
            else:
                ans.append([s2,f2])
        return ans
