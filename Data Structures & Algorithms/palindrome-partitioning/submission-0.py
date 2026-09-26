class Solution:
    def partition(self, s: str) -> List[List[str]]:        
        output = []
        sol = []
        n = len(s)

        def isPalindrome(s, l , r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i == n:
                output.append(sol[:])
                return

            for j in range(i, n): #just for partitioning
                if isPalindrome(s, i, j): #was gonna do s[i:j+1] but need helper func
                    sol.append(s[i:j+1]) #exclusive slicing
                    #the rest and backtrack (following the state space tree)
                    backtrack(j+1)
                    sol.pop()

        backtrack(0)
        return output        
