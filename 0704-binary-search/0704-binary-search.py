class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0 
        last = len(nums)-1
        while(first<=last):
            mid = (first+last)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                last = mid-1
            else:
                first = mid+1
                
        return -1