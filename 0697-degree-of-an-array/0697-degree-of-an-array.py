class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hm = {}
        minDist = math.inf
        degree = 0
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]].append(i)
            else:
                hm[nums[i]] = [i]
        for k in hm.keys():
            if len(hm[k]) > degree:
                degree = len(hm[k])
        if degree == 1:
            return 1
        for k in hm.keys():
            if len(hm[k]) == degree:
                dist = hm[k][-1] - hm[k][0] + 1
                if dist < minDist:
                    minDist = dist
        return minDist
                
                
        
        