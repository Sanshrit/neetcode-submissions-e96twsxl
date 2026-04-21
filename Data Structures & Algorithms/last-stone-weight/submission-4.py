import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap,-1*x)

        while len(heap) > 1:
            s1 = -1* heapq.heappop(heap)
            s2 = -1*heapq.heappop(heap)
            if s1 > s2:
                heapq.heappush(heap,-1*(s1-s2))
            if s1 < s2:
                heapq.heappush(heap,-1*(s2-s1))
        
        if heap:
            return -1* heapq.heappop(heap)
        return 0