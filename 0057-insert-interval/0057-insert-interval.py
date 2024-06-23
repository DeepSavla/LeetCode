class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals)
        print(intervals)
        resInt = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= resInt[-1][1]:
                if intervals[i][1] > resInt[-1][1]:
                    resInt[-1][1] = intervals[i][1]
            else:
                resInt.append(intervals[i])
        return resInt
        