class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r)// 2

            #*inflection point 
            if nums[mid] > nums[r]: # take a look at input nums = [3, 4, *5, 6, 1, 2]
                l = mid + 1
            else: # nums = [4, 5, *0, 1, 2, 3]
                r = mid 
            # untill the list is logically exhausted to [_]    
        return nums[l]           
