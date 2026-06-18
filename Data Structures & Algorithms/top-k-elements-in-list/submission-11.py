class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m1 = {}
        for x in nums:
            if x in m1:
                m1[x]+=1
            else:
                m1[x]=1

        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for x in m1.keys():
            buckets[m1[x]].append(x)
        ans = []

        for i in range(len(buckets)-1,-1,-1):
            for x in buckets[i]:
                if len(ans) == k:
                    break
                ans.append(x)
        return ans