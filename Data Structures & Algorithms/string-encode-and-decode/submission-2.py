class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + '#' + string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        
        #need placeholder to spot '#' append string (i:j) after that
        i = 0
        j = 0
        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1 # past '#' 
            j = i + length
            output.append(s[i:j])
            i = j  # begin at new int ''
        return output       
