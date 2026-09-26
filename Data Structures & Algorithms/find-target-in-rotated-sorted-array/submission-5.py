class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # find inflection point to know where to split binary search into 2 chunks
        while l < r:
            mid = (l + r)// 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        inflection = l

        #Typical binary search
        def binary_search(l: int, r: int) -> int:
            while l <= r:
                mid = (l + r)// 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        # first chunk of sorted array
        output = binary_search(0, inflection - 1)
        if output != -1:
            return output

        # second chunk(after inflection)
        return binary_search(inflection, len(nums) - 1)



        
        
        