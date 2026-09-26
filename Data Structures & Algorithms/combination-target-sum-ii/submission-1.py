class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        sol, output = [], []
        candidates.sort()

        def backtrack(i, total):
            #1 base case of when target is found and basic when i == n or total > target
            if total == target:
                output.append(sol[:])
                return
            if i == n or total > target:
                return
            
            #2 (not take <-  -> take)
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            backtrack(next_i, total)
            
            sol.append(candidates[i])
            backtrack(i+1, total + candidates[i]) # *i+1
            sol.pop()
        #3
        backtrack(0, 0)
        return output