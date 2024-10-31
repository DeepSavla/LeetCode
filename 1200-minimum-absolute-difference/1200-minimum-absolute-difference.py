class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res =[]
        arr = sorted(arr)
        minDist = math.inf
        for i in range(len(arr)-1):
            curDist = abs(arr[i]-arr[i+1])
            if  curDist< minDist:
                res = [[arr[i],arr[i+1]]]
                minDist = curDist
            elif curDist == minDist:
                res.append([arr[i],arr[i+1]])
        return res
                
        