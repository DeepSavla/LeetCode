import math
class Solution:
    def returnHours(self, piles, mid):
        hours=0
        for p in piles:
            hours = hours + math.ceil(p/mid)
        return hours
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        if h==len(piles):
            return high
        low=1
        while low<high:
            mid = (high + low) // 2
            hours = self.returnHours(piles, mid)
            if hours <= h:
                high=mid
            if hours > h:
                low=mid+1
        return high