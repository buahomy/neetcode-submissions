class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_freq_list = [0] * 26 #index 0 -> 'a', ... index 25 ->'z'

        for i in range(len(s)):
            letter_freq_list[ord(s[i]) - ord('a')] += 1  
            letter_freq_list[ord(t[i]) - ord('a')] -= 1

        for count in letter_freq_list: #each by each in the list
            if count != 0:
                return False
        return True        

        