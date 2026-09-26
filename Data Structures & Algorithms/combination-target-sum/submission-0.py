class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(i, curr, total): #curr-> list, total-> int
            if total == target:
                output.append(curr[:])
                return 
            if i >= len(nums) or total > target:
                return 

            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])  #* 
            curr.pop()# again if index out of bound -> undo(backtracking)  
            backtrack(i+ 1, curr, total) # explore further

        backtrack(0, [], 0)#called
        return output
            