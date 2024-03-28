import math
class Solution:
    def returnHours(self, piles, mid):
        hours=0
        for p in piles:
            hours = hours + math.ceil(p/mid)
        return hours
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        low=1
        rate=high
        if h==len(piles):
            return high
        while low<=high:
            mid = (low+high)//2
            if self.returnHours(piles,mid)<=h:
                high=mid-1
                rate = min(rate, mid)
            else:
                low=mid+1
        return rate
            
        