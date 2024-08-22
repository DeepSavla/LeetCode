class Solution:
    def rob(self, nums: List[int]) -> int:
        def getMaxTotal(arr):   #helper function
            totalTillNow = arr.copy()
            for i in range(2,len(arr)):
                maxVal = 0
                previous1= totalTillNow[i-2]
                prevoius2=0
                if i-3>=0:
                    prevoius2 = totalTillNow[i-3]
                maxVal = max(previous1, prevoius2)
                totalTillNow[i] = maxVal + arr[i]
            return max(totalTillNow)
        
        if len(nums)==1:
            return nums[0]
        t1 = getMaxTotal(nums[:len(nums)-1:])
        t2 = getMaxTotal(nums[1::])
        return max(t1,t2)
        