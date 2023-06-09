class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum=0
        maxSum=0
        for i in range(len(nums)):
            sum=sum +nums[i]
            if i==k-1:
                    maxSum=sum
            if i>=k:
                sum=sum-nums[i-k]
            maxSum = max(maxSum,sum)
        print(maxSum)
        return(float(maxSum)/float(k))
                    
            
        
        