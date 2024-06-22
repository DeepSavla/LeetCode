class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = itemgetter(1))
        minRemove = 0
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<end:
                minRemove+=1
            else:
                end = intervals[i][1]
        return minRemove