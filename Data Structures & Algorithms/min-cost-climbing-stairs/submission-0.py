class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = defaultdict(int)
        n = len(cost)

        def dfs(n):
            if n<= 1:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
            return memo[n]
        return dfs(n)    
            

