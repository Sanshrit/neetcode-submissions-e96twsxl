class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def dist(point):
            x1,y1 = point
            return math.sqrt((x1)**2 + (y1)**2)
        
        for p in points:
            heap.append((dist(p),p))
        
        heapq.heapify(heap)
        ans = []
        while k:

            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans