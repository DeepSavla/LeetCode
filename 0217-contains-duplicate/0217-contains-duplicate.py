class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        TLE - Brute force:
        
        dict={}
        for num in nums:
            if num in dict.keys():
                return True
            else:
               dict[num] = 0
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
        