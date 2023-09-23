import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals)
        queue = [intervals[0][1]]
        heapq.heapify(queue)
        for i in range(1,len(intervals)):
            if queue[0] <= intervals[i][0]:
                heapq.heappop(queue)
            heapq.heappush(queue,intervals[i][1])
        return len(queue)


        