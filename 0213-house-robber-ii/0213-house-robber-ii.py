class Solution:
    def rob(self, nums: List[int]) -> int:
        def getMaxTotal(arr):
            totalTillNow = arr.copy()
            for i in range(1,len(arr)):
                maxVal = 0
                for j in range(i-1):
                    maxVal = max(maxVal, totalTillNow[j])
                totalTillNow[i] = maxVal + arr[i]
            print(totalTillNow)
            return max(totalTillNow)
        
        if len(nums)==1:
            return nums[0]
        t1 = getMaxTotal(nums[:len(nums)-1:])
        t2 = getMaxTotal(nums[1::])
        print(t1)
        print(t2)
        return max(t1,t2)
        