class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # Snap
        sumOfNums = sum(nums)
        if (target + sumOfNums) % 2 != 0 or abs(target) > sumOfNums:
            return 0
        sumPositive = (target + sumOfNums)// 2    

        #2
        n = len(nums)
        dp = [[0] * (sumPositive + 1) for _ in range(n+1)]

        #1
        for item in range(n + 1):
            dp[item][0] = 1
        for summ in range(1, sumPositive + 1):
            dp[0][summ] = 0

        #3 Recurrence Relation
        for item in range(1, n + 1):
            for summ in range(sumPositive + 1):
                dp[item][summ] = dp[item - 1][summ]
                if summ >= nums[item - 1]:
                    dp[item][summ] = dp[item][summ] + dp[item - 1][summ - nums[item - 1]]

        return dp[n][sumPositive]            