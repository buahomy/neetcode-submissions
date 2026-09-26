class Solution:

    def climbStairs(self, n: int) -> int:
        
        #dfs memo
        memo = defaultdict(int)
        def dfs(n):
            if n in memo:
                return memo[n]

            if n <= 2:
                memo[n] = n
            else:
                memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]    
            
        return dfs(n)            