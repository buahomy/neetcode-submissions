class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_finish(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) #rounded up
            
            return hours <= h 

        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r)//2
            if k_finish(mid):
                r = mid
            else:
                l = mid + 1
        return l        
        