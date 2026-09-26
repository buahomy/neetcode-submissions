class MedianFinder:

    # Raw Object Sorting
    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        self.array.sort()
        n = len(self.array)
        return (self.array[n//2]) if (n & 1) else ((self.array[n//2] + self.array[(n//2) -1])/2) 