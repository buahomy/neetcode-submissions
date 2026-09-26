class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = [num ** 2 for num in nums]
        output = []

        pointer1, pointer2 = 0, len(nums) - 1
        while pointer1 < pointer2:
            if square[pointer1] > square[pointer2]:
                output.append(square[pointer1])
                pointer1 += 1
            else:
                output.append(square[pointer2])
                pointer2 -= 1
        output.append((square[pointer1]))
            
        return output[::-1]
