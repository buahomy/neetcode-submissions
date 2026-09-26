class Solution:
    
    def __init__(self):
        # base cases
        self.memo = {1:1, 2:2} #avoid happening in every call inside climbStairs()

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        # main
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

        