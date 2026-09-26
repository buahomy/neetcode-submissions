class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        #2
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        #1 -> base case
        dp[0][0] = 0
        for summ in range(1, amount + 1):
            dp[0][summ] = float('inf')
        for item in range(1, n + 1):
            dp[item][0] = 0

        #3 Recurrence relation
        for item in range(1, n + 1):
            for summ in range(1, amount + 1):
                # Not take
                dp[item][summ] = dp[item - 1][summ]
                # Take (with condition)
                if summ >= coins[item - 1]:
                    dp[item][summ] = min(dp[item - 1][summ], 1 + dp[item][summ - coins[item - 1]])

        return dp[n][amount] if dp[n][amount] != float('inf') else -1           

   
        



