class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSubRev = {}
        sum = 0
        for i in range(len(nums)):
            a = nums[i] - int(str(nums[i])[::-1])
            if a in numSubRev.keys():
                numSubRev[a] = numSubRev[a] + 1
            else:
                numSubRev[a] = 1
        for k in numSubRev.keys():
            sum = sum + (numSubRev[k] * (numSubRev[k]-1))//2
        return sum % (pow(10,9) + 7)
            
            