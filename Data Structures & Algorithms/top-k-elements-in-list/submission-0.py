class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1 #or if just use {} for dict with no safety, can add to be safe in this line with freq_dict[num] = 1 + freq_dict.get(num, 0)

        heap = []
        for num, freq in freq_dict.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

            output = [num for freq, num in heap] #or just for typical loop 
        return output    

    
    