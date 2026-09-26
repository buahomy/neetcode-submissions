class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        output = []
        sol = []
        n = len(digits)

        mapping = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

        def backtrack(i):
            if i == n:
                output.append(''.join(sol))
                return

            for char in mapping[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()
                    
        backtrack(0)
        return output            
