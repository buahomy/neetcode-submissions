class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # dumb way (brute-force)
        output = []
        for i in range(len(nums)):
            subarray = nums[:i] + nums[i+1:]
            product = 1
            for num in subarray:
                product *= num
            output.append(product)
        return output        