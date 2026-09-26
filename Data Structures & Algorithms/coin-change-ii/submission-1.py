class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        #2
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        #1 Base case
        for item in range(n + 1):
            dp[item][0] = 1
        for summ in range(1, amount + 1):
            dp[0][summ] = 0

        #3 Recurrence relation
        for item in range(1, n + 1):
            for summ in range(1, amount + 1):
                # Not take
                dp[item][summ] = dp[item - 1][summ]
                # Take
                if summ >= coins[item - 1]:
                    dp[item][summ] += dp[item][summ - coins[item - 1]]

        return dp[n][amount] 