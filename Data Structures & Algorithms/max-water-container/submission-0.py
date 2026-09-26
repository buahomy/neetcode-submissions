class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer1, pointer2 = 0, len(heights) - 1
        currMax = 0
        while pointer1 < pointer2:
            x = pointer2 - pointer1
            
            if heights[pointer1] <= heights[pointer2]:
                lower = heights[pointer1]
                pointer1 += 1
                area = lower * x
                currMax = max(currMax, area)
            else:
                lower = heights[pointer2]
                pointer2 -= 1
                area = lower * x
                currMax = max(currMax, area)
        return currMax        
        