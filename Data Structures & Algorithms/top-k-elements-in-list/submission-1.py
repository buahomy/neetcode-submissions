class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1 #or if just use {} for dict with no safety, can add to be safe in this line with freq_dict[num] = 1 + freq_dict.get(num, 0)

        #bucket sort
        freq_bucket = [[] for i in range(len(nums) + 1)] #list of empty buckets
        for num, freq in freq_dict.items():
            freq_bucket[freq].append(num)

        output = [num for i in range(len(freq_bucket) - 1, 0, -1) for num in freq_bucket[i]]
        return output[:k]    
    