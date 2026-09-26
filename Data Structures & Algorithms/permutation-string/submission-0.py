class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False

        #freq list
        freqS1 = [0] * 26
        freqS2 = [0] * 26
        for i in range(l1):
            freqS1[ord(s1[i]) - ord('a')] += 1
            freqS2[ord(s2[i]) - ord('a')] += 1

        if freqS1 == freqS2:
            return True

        # second pass(inclusive from len(s1)) >> slide the window in each iteration
        for i in range(l1, l2):
            freqS2[ord(s2[i]) - ord('a')] += 1 
            freqS2[ord(s2[i - l1]) - ord('a')] -= 1
            if freqS1 == freqS2:
                return True

        return False             
        