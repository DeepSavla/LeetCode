class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = [intervals[0]]
        endList = []
        for i in range(1,len(intervals)):
            if intervals[i][0]<=result[-1][1]:
                if intervals[i][1]>=result[-1][1]:
                    result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])
        return result