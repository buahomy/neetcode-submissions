class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s, dict_t = {}, {}

        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0) #map value to key, use .get() to be safe on counting
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

        if dict_s != dict_t:
            return False
        return True        

        