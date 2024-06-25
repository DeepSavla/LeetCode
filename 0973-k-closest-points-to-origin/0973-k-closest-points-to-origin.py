class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points)==k:
            return points
        closestArr = []
        heapq.heapify(closestArr)
        for i in range(len(points)):
            dist = points[i][0]**2+points[i][1]**2
            dist = dist*-1
            if len(closestArr)>=k:
                if closestArr[0][0] < dist:
                    rem = heapq.heappop(closestArr)
                    heapq.heappush(closestArr,(dist,i))
            else:
                heapq.heappush(closestArr,(dist,i))
                
        res = []
        for p in closestArr:
            res.append(points[p[1]])
        return res