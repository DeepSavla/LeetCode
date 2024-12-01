class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        winTotal = 0
        reqTotal = k*threshold
        l=0
        r=k-1
        for i in range(k):
            winTotal = winTotal+arr[i]
        if winTotal >=reqTotal:
            res +=1
        while r<len(arr)-1:
            r += 1
            l+=1
            winTotal = winTotal + arr[r] - arr[l-1]
            print(winTotal)
            if winTotal >=reqTotal:
                res+=1
        return res
            
        
        