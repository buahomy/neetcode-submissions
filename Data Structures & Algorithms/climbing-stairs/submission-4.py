class Solution:

    def climbStairs(self, n: int) -> int:
        
        #dfs memo
        hashMap = defaultdict(int)
        def dfs(n):
            if n <= 2:
                hashMap[n] = n
            else:
                hashMap[n] = dfs(n-1) + dfs(n-2)
            return hashMap[n]    
            
        return dfs(n)            