class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            #check for overlap
            s1,f1 = ans[-1]
            s2,f2 = intervals[i]

            if f1>=s2:
                ans[-1][1] = max(f1,f2)
            else:
                ans.append(intervals[i])
        return ans