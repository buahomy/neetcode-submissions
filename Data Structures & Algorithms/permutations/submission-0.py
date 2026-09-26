class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        sol = []
        n = len(nums)

        def backtrack():
            if len(sol) == n:
                output.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        backtrack()

        return output                