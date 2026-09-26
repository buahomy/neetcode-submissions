class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col = len(matrix), len(matrix[0])

        low, high = 0, (row * col) - 1
        while low <= high:
            mid = (low + high)//2
            midVal = matrix[mid // col][mid % col]
            # it'd work seemlessly (tested w/ Example 1)
            if target < midVal:
                high = mid-1
            elif target > midVal:
                low = mid+1
            else:
                return True
        return False


