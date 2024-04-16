class Solution:
    def timeTaken(self, speed, piles):
        time = 0
        for i in range(len(piles)):
            time = time + ceil(piles[i]/speed)
        return time
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        minInteger = j
        while i<=j:
            mid = (i+j)//2
            time = self.timeTaken(mid,piles)
            if time <= h:
                minInteger = min(mid, minInteger)
                j=mid-1
            else:
                i=mid+1
        return minInteger
        