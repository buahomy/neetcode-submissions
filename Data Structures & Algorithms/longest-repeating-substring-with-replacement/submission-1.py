class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        set = {}
        l = 0
        maxCharFreq = 0 
        currMaxLength = 0

        for r in range(len(s)):
            set[s[r]] = set.get(s[r], 0) + 1
            maxCharFreq = max(maxCharFreq, set[s[r]]) #dict[s[r]] 

            if (r - l + 1) - maxCharFreq > k: 
                set[s[l]] -= 1
                l += 1

            currMaxLength = max(currMaxLength, r - l + 1) 
        return currMaxLength   
        