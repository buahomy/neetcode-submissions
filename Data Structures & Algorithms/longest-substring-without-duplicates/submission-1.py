class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set = {}
        l = 0
        currMaxLength = 0

        for r in range(len(s)):
            if s[r] in set:
                l = max(set[s[r]] + 1, l) #shrink the valid window s[r] + 1
            set[s[r]] = r #key -> each string, value -> its index
            currMaxLength = max(currMaxLength, r - l + 1)

        return currMaxLength

