class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        # a*, l, r
        for i, beginNum in enumerate(nums):

            if beginNum > 0:
                break
            if i > 0 and beginNum == nums[i - 1]:
                continue
                
            pointer1, pointer2 = i + 1, len(nums) - 1
            while pointer1 < pointer2:
                if beginNum + nums[pointer1] + nums[pointer2] < 0:
                    pointer1 += 1
                elif pointer1 < pointer2 and beginNum + nums[pointer1] + nums[pointer2] > 0:
                    pointer2 -= 1
                else:
                    output.append([beginNum, nums[pointer1], nums[pointer2]])	

                    pointer1 += 1
                    pointer2 -= 1 
                    while pointer1 < pointer2 and nums[pointer1] == nums[pointer1 - 1]: 
                        pointer1 += 1
        return output	


