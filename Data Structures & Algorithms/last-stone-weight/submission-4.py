class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0
        if len(stones) == 1:
            return 1
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            heapq.heappush(stones, -abs(a - b))
        return -stones[0]
