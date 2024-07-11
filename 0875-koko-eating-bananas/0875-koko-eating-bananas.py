class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate(rate):
            t = 0
            for p in piles:
                t = t+ ceil(p/rate)
            return t
    
        if h==len(piles):
            return max(piles)
        low=1
        high=max(piles)
        while 1:
            mid = (low+high)//2
            if calculate(mid)>h:
                low = mid+1
            else:
                if mid!=1 and calculate(mid-1)<=h:
                    high=mid-1
                else:
                    return mid
                    break
                