class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x] = 1
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for x in freq.keys():
            buckets[freq[x]].append(x)
        
        ans = []
        for i in range(n,-1,-1):
            x = buckets[i]
            for num in x:
                if k:
                    ans.append(num)
                    k-=1
        return ans