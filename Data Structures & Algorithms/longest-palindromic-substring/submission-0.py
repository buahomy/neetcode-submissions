class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""

        n = len(s)
        start = 0
        max_len = 1

        for i in range(n):
            for j in range(i, n):
                substr = s[i:j+1]
                if substr == substr[::-1] and (j - i + 1) > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start + max_len]



        