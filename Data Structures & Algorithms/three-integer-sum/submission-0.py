class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        # a*, l, r
        for i, a in enumerate(nums):
            if a > 0: #no possible sum of 0 as the lowest is 1,..
                break
 
            if i > 0 and a == nums[i-1]: # avoid the same starting number to avoid the duplicate triplets
                continue

            #begin
            l, r = i + 1, len(nums) - 1   
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                # triplet with sum of 0 found    
                else: 
                    output.append([a, nums[l], nums[r]])
                    # both l r used already -> find other possible combos in O(n^2)
                    l += 1 
                    r -=1
                    # now, account for second repeated value like [-1, 0, 0, 0, 1] where it'd create 3 duplicate triplets of [-1, 0, 1]
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return output                


