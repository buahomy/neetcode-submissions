class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # either not rob take max(left) or rob(right)
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 


        return dp[-1] #take last element of dp (max amount)
            
                        

