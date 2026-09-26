class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #in-n-out burger
        if not s:
            return ""

        n = len(s)
        # can't maxLen = 1 cause it'd keep update start & end
        maxLen = 1
        # make sure it's defined before the loop ( if no longer palindrome is found, we still return something valid at the end)
        start = 0  

        for i in range(n):    
            
            palinOdd = self.expand(s, i, i)
            palinEven = self.expand(s, i, i + 1)
            currMaxLen = max(palinOdd, palinEven)

            # start and end based on mid i 
            if currMaxLen > maxLen:
                start = i - (currMaxLen - 1)//2
                end = i + (currMaxLen)//2
                maxLen = currMaxLen
        return s[start:start + maxLen] 

    def expand(self, s: str, l: int, r:int) -> int:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1 #len of possible valid palin (because it'd out of range once finished)        
        



        