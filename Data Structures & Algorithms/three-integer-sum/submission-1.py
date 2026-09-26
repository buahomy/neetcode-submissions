class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        # i, j, target*
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1

        for i in range(len(nums)):
            dict[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]: # care(s)
                continue

            for j in range(i+1, len(nums)):
                dict[nums[j]] -= 1 #decrement to check all possible combos towards the right
                if j - 1 > i and nums[j] == nums[j-1]: # care(s)
                    continue
                target = -(nums[i] + nums[j])
                if dict[target] > 0 and nums[i] + nums[j] + target == 0:
                    output.append([nums[i], nums[j], target])        

            for j in range(i+1, len(nums)): # put it back so that can be used as next i
                dict[nums[j]] += 1
        return output        
