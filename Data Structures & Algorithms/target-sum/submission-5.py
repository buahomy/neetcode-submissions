class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (target + total) % 2 != 0:
            return 0
        sumPositive = (target + total) // 2

        n = len(nums)
        dp = [[0] * (sumPositive + 1) for _ in range(n + 1)]

        # Base case
        dp[0][0] = 1

        # Recurrence
        for item in range(1, n + 1):
            for summ in range(sumPositive + 1):
                dp[item][summ] = dp[item - 1][summ]
                if summ >= nums[item - 1]:
                    dp[item][summ] += dp[item - 1][summ - nums[item - 1]]

        return dp[n][sumPositive]           