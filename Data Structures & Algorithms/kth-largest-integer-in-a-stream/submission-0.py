class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k
        heapq.heapify(self.stream)
        while len(self.stream) > k:
            heapq.heappop(self.stream)      

    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        else:
            heapq.heappushpop(self.stream, val)
        return self.stream[0]                    
