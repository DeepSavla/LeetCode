class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimizedMaxSum = 0
        nums = sorted(nums)
        l = len(nums)
        for i in range(l/2):
            curMax = nums[i] + nums[l - 1 -i]
            minimizedMaxSum = max(minimizedMaxSum,curMax)
        return minimizedMaxSum
            
            
        