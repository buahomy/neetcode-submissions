class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        #s1
        charFreq1 = Counter(s1)
        charFreq2 = Counter(s2[:l1])
        if charFreq1 == charFreq2:
            return True

        #s2 to slide
        for i in range(l1, l2):
            addToWinChar = s2[i]
            removeFromWinChar = s2[i - l1]

            charFreq2[addToWinChar] += 1
            charFreq2[removeFromWinChar] -= 1
            if charFreq1 == charFreq2:
                return True
            else:
                continue
        return False        
