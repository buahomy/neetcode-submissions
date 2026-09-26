class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1 
        #{1:1, 2:2, 3:3}
        
        reversed_list = [(v, u) for u,v in freq_dict.items()]
        heapq.heapify(reversed_list)
        while len(reversed_list) > k:
            heapq.heappop(reversed_list)
        return [value for (_, value) in reversed_list]


           
    