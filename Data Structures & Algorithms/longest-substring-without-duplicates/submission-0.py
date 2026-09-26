class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        validWindow = set()
        l = 0
        currMaxLength = 0

        for r in range(len(s)):
            while s[r] in validWindow:
                validWindow.remove(s[l])
                l+= 1
            validWindow.add(s[r])
            currMaxLength = max(currMaxLength, r - l + 1)

        return currMaxLength

