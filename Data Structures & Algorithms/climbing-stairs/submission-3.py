class Solution:

    # Bottom-up >> 1-D array/ compute from smaller to larger in order
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        
        #base cases
        dp[1], dp[2] = 1, 2

        # main
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]    
        

        