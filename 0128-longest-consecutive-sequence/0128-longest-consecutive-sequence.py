class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxLen=0
        for dig in nums:
            curMax=1
            if dig-1 in nums:
                continue
            while dig+1 in nums:
                curMax = curMax + 1
                dig = dig + 1
            maxLen = max(maxLen , curMax)
        return maxLen
                