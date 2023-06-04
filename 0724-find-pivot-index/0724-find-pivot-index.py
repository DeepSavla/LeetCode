class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum=0
        rightSum= sum(nums)
        for j in range(len(nums)):
            leftSum = leftSum + nums[j]
            if j!=0:
                rightSum = rightSum - nums[j-1]
            if leftSum == rightSum:
                return j
        return -1
