class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        halfSum = total // 2

        #Get var2: int(indirectly create one self)
        halfSum = 0
        for num in nums:
            halfSum += num
        halfSum = halfSum // 2

        # 0/1 Knapsack
        #2
        n = len(nums) # for duplicating rows down (items)
        dp = [[False] * (halfSum + 1) for _ in range(n + 1)] 

        #1 base case
        for item in range(n + 1):
            dp[item][0] = True
        for hS in range(1, halfSum + 1):
            dp[0][hS] = False

        #3 Recurrence
        for item in range(1, n + 1): #row
            for hS in range(1, halfSum + 1): # col
                #Take (with the condition that item in nums would not overfill the hS)
                if hS >= nums[item - 1]: # - 1 due to the indexing (+ 1 initilized earlier)
                    # Not take or Take
                    dp[item][hS] = dp[item - 1][hS] or dp[item - 1][hS - nums[item - 1]]
                else:
                    dp[item][hS] = dp[item - 1][hS]
        return dp[n][halfSum]             
