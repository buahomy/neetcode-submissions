class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        palinCount = 0

        for i in range(n):
            palinCount += self.expand(s, i, i)    
            palinCount += self.expand(s, i, i+1)

        return palinCount

    def expand(self, s: str, l: int, r: int) -> int:
        # to detect grouped palin
        count = 0
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1 # count every single of each substring 
            l -= 1
            r += 1
        return count      

        