class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        sol, output = [], []

        def backtrack(i, total): #curr-> list, total-> int
            if total == target:
                output.append(sol[:])
                return 
            if i >= len(nums) or total > target:
                return 

            backtrack(i+1, total) 

            sol.append(nums[i])
            backtrack(i, total + nums[i])  
            sol.pop()  

        backtrack(0, 0)#called
        return output
            