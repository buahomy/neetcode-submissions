class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for str in strs: # extra thing to loop through every str of strs
            letter_freq_list = [0] * 26
            for letter in str:
                letter_freq_list[ord(letter) - ord('a')] += 1
            output[tuple(letter_freq_list)].append(str)
        return list(output.values())    
        