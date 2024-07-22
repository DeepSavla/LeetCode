#this algo is called kadane's algo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]
        i=1
        while i<len(nums):
            if curSum <0:
                curSum = nums[i]
            else:
                curSum = curSum + nums[i]
            maxSum = max(maxSum, curSum)
            i+=1
        return maxSum
        