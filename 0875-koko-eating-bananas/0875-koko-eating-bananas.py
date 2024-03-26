import math
class Solution:
    def returnHours(self, piles, mid):
        hours=0
        if mid>0:
            for p in piles:
                hours = hours + math.ceil(p/mid)
        return hours
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        low=1
        if h==len(piles):
            return high
        while low<high:
            mid = (high + low) // 2
            hours = self.returnHours(piles, mid)
            if hours == h:
                while self.returnHours(piles, mid-1) == h:
                    mid=mid-1
                return mid
            if hours < h:
                high=mid-1
            if hours > h:
                low=mid+1
        while hours>h:
            mid=mid+1
            hours = self.returnHours(piles, mid)
        while hours<h and self.returnHours(piles, mid-1)<h and mid>1:
            mid = mid-1
            hours = self.returnHours(piles, mid)
        return mid
    
                