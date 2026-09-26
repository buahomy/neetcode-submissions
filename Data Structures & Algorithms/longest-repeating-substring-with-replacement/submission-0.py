class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = defaultdict(int)
        l = 0
        maxCharFreq = 0 #keep track of string in s that has the most freq
        currMaxLength = 0

        for r in range(len(s)):
            dict[s[r]] += 1
            maxCharFreq = max(maxCharFreq, dict[s[r]]) #dict[s[r]] 

            #valid replacement k 
            if (r - l + 1) - maxCharFreq > k: # windown size - mostFreqChar -> no. of replacements needed  
                # shrink the window(also deduct value from dict)
                dict[s[l]] -= 1
                l += 1

            currMaxLength = max(currMaxLength, r - l + 1) 
        return currMaxLength   
        