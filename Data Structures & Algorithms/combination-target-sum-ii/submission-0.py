class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        sol = []

        def backtrack(i, remaining):
            if remaining == 0:
                output.append(sol[:])
                return

            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                if candidates[j] > remaining:
                    break

                sol.append(candidates[j])
                backtrack(j + 1, remaining - candidates[j])
                sol.pop()
                prev = candidates[j]

        backtrack(0, target)
        return output            
