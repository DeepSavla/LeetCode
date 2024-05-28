import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i]*-1 #workaround to get largest in priority queue
        heapq.heapify(stones)
        while len(stones)>1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            res = s1-s2
            if res!=0:
                heapq.heappush(stones,res)
        if len(stones)!=0:
            return -1*stones[0]
        return 0
            