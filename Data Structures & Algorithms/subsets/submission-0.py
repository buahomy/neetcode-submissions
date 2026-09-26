class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        sol = []
        
        #state space tree
        def backtrack(i):
            
            #base case to stop the power
            if i == n:
                output.append(sol[:])
                return

            #no, not take
            backtrack(i+1) 

            #yes, take
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)    
        return output