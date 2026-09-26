class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1, pointer2 = 0, len(numbers) - 1
        while pointer1 < pointer2:
            sumNum  = numbers[pointer1] + numbers[pointer2]
            if sumNum == target:
                return [pointer1+1, pointer2+1]
            elif sumNum > target:
                pointer2 -= 1
            else:
                pointer1 += 1