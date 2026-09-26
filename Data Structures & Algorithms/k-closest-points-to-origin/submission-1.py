class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        index = 0
        for i, j in points:
            dist = -math.sqrt(i**2 + j**2)
            max_heap.append((dist, index))
            index += 1

        heapq.heapify(max_heap)
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        i = max_heap[0][1]
        return [points[i] for (_, i) in max_heap]