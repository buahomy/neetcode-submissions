class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
                
        sth = []
        index = 0
        for x, y in points:
            sth.append((math.sqrt(x**2+y**2), index))
            index += 1

        sth.sort()

        output = []
        for i in range(k):
            minIndex = sth[i][1]
            output.append(points[minIndex])
            
        return output  