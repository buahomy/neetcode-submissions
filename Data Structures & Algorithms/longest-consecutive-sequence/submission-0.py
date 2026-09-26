class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
            
        s = set(nums)
        currMax = 0
        for num in nums:

            if num - 1 not in s:
                count = 1
                nextVal = num + 1
                while nextVal in s:
                    count += 1
                    nextVal += 1

                currMax = max(currMax, count)

        return currMax

                