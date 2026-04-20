class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        for num in nums:
            if num in d1:
                d1[num]+=1
            else:
                d1[num] = 1
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for item in d1.keys():
            buckets[d1[item]].append(item)


        ans = []
        for i in range(n,0,-1):
            for num in buckets[i]:
                if k:
                    ans.append(num)
                    k-=1
        return ans